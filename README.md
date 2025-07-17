📸 Face Recognition Attendance System

This is a real-time **Face Recognition-based Attendance System** built using **Python** and **OpenCV**. It uses the `face_recognition` library to detect and recognize faces from webcam input and automatically logs attendance into a `.csv` file.

---

🔧 Features

- Detects and recognizes faces using webcam input.
- Automatically logs attendance with **name** and **timestamp**.
- Generates **subject-wise** and **date-wise** attendance reports in CSV format.
- Prevents duplicate attendance entries in a single session.
- Allows the user to select the subject through a command-line interface.

---

🛠️ Technologies and Libraries

- `OpenCV` – For video capture and display.
- `face_recognition` – For face detection and facial embeddings.
- `NumPy` – For array and numerical operations.
- `Pandas` – For structured data handling and CSV writing.
- `datetime` – For date and time logging.
- `os`, `sys` – For file handling and user interaction.

---

📁 Folder Structure
```
project_directory/
│
├── photos/ # Folder containing known faces
│ ├── person1.jpg # Image (filename used as label)
│ └── person2.png
│
├── face_recognition_project.py # Main script
├── CNCC-2025-06-15.csv # Auto-generated attendance file (example)
```


---

📌 Note

- Create a folder named **`photos/`** in the same directory as the Python script.
- Add clear front-facing images of each person you want to recognize.
- The **filename (without extension)** will be used as the person's name in the attendance log.
  - Example: `john.jpg` → "john" will appear in the CSV.

---

🚀 How to Run

1. Ensure you have the `photos/` folder with labeled images:
2. Install the required libraries: pip install opencv-python face_recognition numpy pandas
3. Run the script:python face_recognition_project.py
4. Select the subject from the menu:
5. Press q to stop the webcam and exit the program.

