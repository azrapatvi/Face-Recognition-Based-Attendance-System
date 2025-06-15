📸 Face Recognition Attendance System

This project is a real-time Face Recognition-based Attendance System implemented using Python and OpenCV. It utilizes the face_recognition library to detect and recognize faces from a webcam feed and logs attendance data in a CSV file.

🔧 Features
Detects and recognizes faces using webcam input.
Stores recognized faces’ names and timestamps.
Generates subject-wise, date-wise attendance records in .csv format.
Ensures duplicate entries are avoided in a session.
Handles user subject selection via command line input.

🛠️ Technologies and Libraries
OpenCV - For video capture and image display.
face_recognition - For face detection and face embedding.
NumPy - For array operations and distance calculations.
Pandas - For structured data storage and CSV file writing.
datetime - For timestamp logging.
os, sys - For file handling and user interaction.

📁 Folder Structure
bash
Copy
Edit
project_directory/
│
├── photos/                      # Folder containing labeled images of known individuals
│   ├── person1.jpg              # The filename (e.g., person1) is used as the label
│   └── person2.png
│
├── face_recognition_project.py  # Main script
├── 1.CNCC-2025-06-15.csv        # Example auto-generated attendance file

📌 Note: You must create a folder named photos/ in the same directory as the script. This folder should contain images of each person you want to recognize. The file name (before .jpg/.png) acts as the label used in attendance logs.

🚀 How to Run
Ensure you have a folder named photos/ with labeled face images (e.g., john.jpg, emma.png).

Install the required libraries:
pip install opencv-python face_recognition numpy pandas

Run the script:
python face_recognition_project.py

Select the subject from the menu:
1. CNCC
2. SEST
3. ML
4. EM
5. ADS
6. Exit

Press q to stop capturing and close the application.

📊 Output
A CSV file named <Subject>-YYYY-MM-DD.csv is created.

Each row includes:
Name of the recognized individual
Timestamp when the face was detected

