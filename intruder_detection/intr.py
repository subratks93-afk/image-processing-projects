import cv2
import numpy as np
import datetime
import os
import winsound
import requests
import pickle
import time
import csv

# ================= CONFIG =================
AUTHORIZED_NAME = "SUBRAT"
CONFIDENCE_THRESHOLD = 70
ALERT_COOLDOWN = 20
CONF_HISTORY_SIZE = 15

BOT_TOKEN = "8659669906:AAGalSMNp8XgfSQqzY4REp54Eyyf_PlQmf4"
CHAT_ID = "6619767086"

IMAGE_DIR = "intruder_images"
LOG_FILE = "access_log.csv"

# ================= LOAD MODELS =================
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

with open("labels.pkl", "rb") as f:
    label_map = pickle.load(f)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# ================= SETUP =================
os.makedirs(IMAGE_DIR, exist_ok=True)

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Name", "Confidence", "Status"])

# ================= FUNCTIONS =================

def send_sos(image_path, timestamp):
    message = f"🚨 SOS ALERT 🚨\nIntruder detected!\nTime: {timestamp}"

    try:
        requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            params={"chat_id": CHAT_ID, "text": message},
            timeout=5
        )

        with open(image_path, "rb") as photo:
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto",
                data={"chat_id": CHAT_ID},
                files={"photo": photo},
                timeout=5
            )

        print("Telegram Alert Sent ✅")

    except Exception as e:
        print("Telegram Error:", e)


def log_event(name, confidence, status):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, name, round(confidence, 2), status])


# ================= CAMERA SETUP =================
cap = cv2.VideoCapture(0)

# Warm-up camera (fix delay)
for _ in range(10):
    cap.read()

cv2.namedWindow("Smart Intruder Detection System", cv2.WINDOW_NORMAL)

# ================= VARIABLES =================
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

        face = cv2.resize(gray[y:y+h, x:x+w], (200, 200))
        label, confidence = recognizer.predict(face)
        name = label_map.get(label, "Unknown")

        # Confidence smoothing
        confidence_history.append(confidence)
        if len(confidence_history) > CONF_HISTORY_SIZE:
            confidence_history.pop(0)

        avg_conf = sum(confidence_history) / len(confidence_history)

        # Unknown handling
        if name == "Unknown":
            avg_conf = 999

        print(f"Predicted: {name} | Avg Confidence: {round(avg_conf, 2)}")

        # ================= DECISION =================
        if name == AUTHORIZED_NAME and avg_conf < CONFIDENCE_THRESHOLD:

            status = "AUTHORIZED"
            color = (0, 255, 0)

            authorized_counter += 1
            intruder_counter = 0

            if authorized_counter > 10:
                log_event(name, avg_conf, status)
                authorized_counter = 0

        else:
            status = "INTRUDER"
            color = (0, 0, 255)

            intruder_counter += 1
            authorized_counter = 0

            if intruder_counter > 20 and time.time() - last_alert_time > ALERT_COOLDOWN:

                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                image_path = os.path.join(IMAGE_DIR, f"intruder_{timestamp}.jpg")

                cv2.imwrite(image_path, frame)
                winsound.Beep(2000, 800)

                send_sos(image_path, timestamp)
                log_event(name, avg_conf, status)

                print("Intruder Alert Sent!")

                last_alert_time = time.time()
                intruder_counter = 0

        # ================= DISPLAY =================
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, status, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow("Smart Intruder Detection System", frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

# ================= CLEANUP =================
cap.release()
cv2.destroyAllWindows()