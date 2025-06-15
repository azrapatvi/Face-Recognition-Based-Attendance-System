import cv2
import face_recognition
import numpy as np
import pandas as pd
from datetime import datetime
import os
import sys

print("select subjects:")
print("1.CNCC")
print("2.SEST")
print("3.ML")
print("4.EM")
print("5.ADS")
print("6.exit")
subject=None


choice=int(input("\nenter your choice:"))

if choice==1:
    subject="1.CNCC"
elif choice==2:
    subject="2.SEST"
elif choice==3:
    subject="3.ML"
elif choice==4:
    subject="4.EM"
elif choice==5:
    subject="5.ADS"
elif choice==6:
    print("exiting...")
    sys.exit()
else:
    print("invalid choice")


def get_today_filename():
    today_date = datetime.now().strftime("%Y-%m-%d")  
    filename = f"{subject}-{today_date}.csv"  
    return filename
print("loading..")


video_capture = cv2.VideoCapture(0)

folder = "photos"

# List of known images and their names
known_face_encodings = []
known_face_names = []

# Load known images and encodings
for filename in os.listdir(folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  # Check for image files
        image_path = os.path.join(folder, filename) #photos/abc.jpg
        known_image = face_recognition.load_image_file(image_path)
        known_encoding = face_recognition.face_encodings(known_image)
        
        if known_encoding:  # Ensure that a face encoding was found
            known_face_encodings.append(known_encoding[0]) 
            known_face_names.append(filename.split('.')[0]) 


df = pd.DataFrame(columns=["Name", "Timestamp"])
detected_names = set()  


current_filename = get_today_filename()

while True:
    ret, frame = video_capture.read()

    if not ret:  
        print("Failed to capture frame.")
        break

    # Convert the image from BGR (OpenCV format) to RGB (face_recognition format)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Find all the faces and face encodings in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the face matches any known face
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]

            if name not in detected_names:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                df = df._append({"Name": name, "Timestamp": current_time}, ignore_index=True)
                detected_names.add(name)  # Mark this name as detected

                # Save to CSV file after each detection
                try:
                    if not df.empty:
                        df.to_csv(current_filename, index=False)
                except PermissionError:
                    print("Error: The file is currently open. Please close it and try again.")

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # Display the resulting image
    cv2.imshow('ATTENDANCE SYSTEM', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
if df.empty:
    print("Unable to create file because there is no data in the .csv file.")

else:
    print(f"Successfully created your: {current_filename}")
    if os.path.exists(current_filename):
        print(os.path.abspath(current_filename))
    else:
        print("No information: File does not exist.")
          
if not df.empty:
    df.to_csv(current_filename, index=False)

video_capture.release()
cv2.destroyAllWindows()

