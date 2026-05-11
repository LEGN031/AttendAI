# 👤 Face Recognition Attendance System

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MIT License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

A high-performance, real-time facial recognition system designed for automated attendance tracking. This project leverages advanced computer vision to identify individuals and log their presence efficiently.

## 📌 Purpose
The main goal of this project is to eliminate the manual effort involved in taking attendance. By using a standard webcam, the system can identify pre-registered individuals and record their arrival time automatically, ensuring accuracy and saving time.

## 💡 Why it is Useful
- **Efficiency:** No more manual signatures or call-outs.
- **Accuracy:** Reduces the risk of human error or "proxy" attendance.
- **Real-time Data:** Instantly logs data into accessible CSV files.
- **Cost-Effective:** Works with standard hardware (webcam and PC).

## 🎯 Main Objectives
1. Implement a robust facial recognition algorithm using `dlib` and `face_recognition`.
2. Develop a real-time monitoring interface with visual feedback.
3. Automate data logging into daily CSV reports.
4. Ensure easy management of "known faces" via a simple folder structure.

## 🛠️ Technologies Used
- **Python:** The core programming language.
- **OpenCV:** For video stream processing and GUI feedback.
- **face_recognition:** Built on `dlib`, used for high-accuracy face identification.
- **NumPy:** For efficient array operations.
- **CSV/Datetime:** For data persistence and timestamping.

## ⚙️ Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/face-recognition-attendance.git
   cd face-recognition-attendance
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare the photos:**
   - Place clear images of people you want to recognize in the `photos/` folder.
   - Name the files with the person's name (e.g., `John_Doe.jpg`).

## 🚀 How to Run
Simply execute the main script:
```bash
python program.py
```
- The system will open a window showing the camera feed.
- Recognized faces will be outlined in green with their names.
- Unknown faces will be outlined in red.
- Press `q` to exit the system.

## 📈 Future Improvements
- **Web Dashboard:** A React/Next.js interface to view attendance records.
- **Database Integration:** Moving from CSV to a robust SQL/NoSQL database.
- **Multi-Camera Support:** Tracking attendance across multiple entry points.
- **Cloud Synchronization:** Automatic backup of reports to the cloud.

---
Developed with ❤️ by [Your Name]
