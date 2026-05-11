import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

video_capture = cv2.VideoCapture(0)

known_encodings = []
known_names = []

# photos_folder = resource_path("photos")
photos_folder = os.path.join(os.getcwd(), "photos")

for filename in os.listdir(photos_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        name = os.path.splitext(filename)[0]         
        name = name.replace("_", " ").title()         

        image = face_recognition.load_image_file(os.path.join(photos_folder, filename))
        encodings = face_recognition.face_encodings(image)

        if encodings:  
            known_encodings.append(encodings[0])
            known_names.append(name)
            print(f"✅ Cargado: {name}")
        else:
            print(f"⚠️  No se encontró cara en: {filename}")

users = known_names.copy()

face_locations = []
face_encodings = []
face_names = []

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

csv_file = os.path.join(os.getcwd(), current_date + ".csv")
f = open(csv_file, "w+", newline="")
w = csv.writer(f)

while True:
    
    ret, frame = video_capture.read()

    if not ret:
        print("No se pudo acceder a la cámara")
        break

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    face_names = []

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_names[best_match_index]
        face_names.append(name)

        if name in known_names and name in users:
            print("User found: " + name)
            users.remove(name)
            now = datetime.now()  
            w.writerow([name, now.strftime("%H:%M:%S")])
            f.flush()  

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)

        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
        cv2.putText(frame, name, (left + 6, bottom - 6),
                    cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)

    cv2.imshow("Attendance System", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()