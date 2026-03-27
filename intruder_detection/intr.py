import cv2
import numpy as np
import datetime
import os
import winsound
import requests
import pickle
import time
import csv

# ================= LOAD FACE MODEL =================
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

with open("labels.pkl", "rb") as f:
    label_map = pickle.load(f)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

AUTHORIZED_NAME = "SUBRAT"
CONFIDENCE_THRESHOLD = 70   # Your tuned threshold

# ================= TELEGRAM FUNCTION =================
def send_sos(image_path, timestamp):
    bot_token = "8329089502:AAHUfn1Nl9qmPl50N9jdBfs4nsOXknmKDY4"
    chat_id = "6619767086"

    message = f"🚨 SOS ALERT 🚨\nIntruder detected!\nTime: {timestamp}"

    try:
        requests.get(
            f"https://api.telegram.org/bot{bot_token}/sendMessage",
            params={"chat_id": chat_id, "text": message},
            timeout=5
        )

        with open(image_path, "rb") as photo:
            requests.post(
                f"https://api.telegram.org/bot{bot_token}/sendPhoto",
                data={"chat_id": chat_id},
                files={"photo": photo},
                timeout=5
            )

        print("Telegram Alert Sent ✅")

    except Exception as e:
        print("Telegram Error:", e)

# ================= CREATE IMAGE FOLDER =================
if not os.path.exists("intruder_images"):
    os.makedirs("intruder_images")

# ================= CREATE LOG FILE =================
log_file = "access_log.csv"

if not os.path.exists(log_file):
    with open(log_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Name", "Confidence", "Status"])

# ================= LOG FUNCTION =================
def log_event(name, confidence, status):
    with open(log_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([timestamp, name, round(confidence, 2), status])

# ================= CAMERA =================
cap = cv2.VideoCapture(0)
cv2.namedWindow("Smart Intruder Detection System", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Smart Intruder Detection System",
                      cv2.WND_PROP_FULLSCREEN,
                      cv2.WINDOW_FULLSCREEN)

confidence_history = []
authorized_counter = 0
intruder_counter = 0
last_alert_time = 0

# ================= MAIN LOOP =================
while cap.isOpened():

    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    for (x, y, w, h) in faces:

        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (200, 200))

        label, confidence = recognizer.predict(face)
        name = label_map.get(label, "Unknown")

        # -------- Confidence Averaging --------
        confidence_history.append(confidence)
        if len(confidence_history) > 15:
            confidence_history.pop(0)

        avg_conf = sum(confidence_history) / len(confidence_history)

        print("Predicted:", name, "| Avg Confidence:", round(avg_conf, 2))

        # -------- Decision Logic --------
        if name == AUTHORIZED_NAME and avg_conf < CONFIDENCE_THRESHOLD:

            text = "AUTHORIZED"
            color = (0, 255, 0)

            authorized_counter += 1
            intruder_counter = 0

            if authorized_counter > 10:
                log_event(name, avg_conf, "AUTHORIZED")
                authorized_counter = 0

        else:
            text = "INTRUDER"
            color = (0, 0, 255)

            intruder_counter += 1
            authorized_counter = 0

            # Trigger alert after stable intruder detection
            if intruder_counter > 20 and time.time() - last_alert_time > 10:

                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                image_path = f"intruder_images/intruder_{timestamp}.jpg"

                cv2.imwrite(image_path, frame)
                winsound.Beep(2000, 800)

                send_sos(image_path, timestamp)
                log_event(name, avg_conf, "INTRUDER")

                print("Intruder Alert Sent!")

                last_alert_time = time.time()
                intruder_counter = 0

        # Draw bounding box
        cv2.rectangle(frame, (x,y), (x+w,y+h), color, 2)
        cv2.putText(frame, text, (x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow("Smart Intruder Detection System", frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

cap.release()
cv2.destroyAllWindows() 