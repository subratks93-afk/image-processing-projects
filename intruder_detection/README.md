🛡️ AI-Based Smart Intruder Detection System

📌 Overview

This project is a real-time surveillance system built using Python and OpenCV. It detects a person through a webcam and checks whether they are authorized using face recognition.

If an unknown person is detected, the system captures the image, triggers an alert, sends a Telegram notification, and logs the event.


🚀 Features

* Detects faces in real-time using a webcam
* Recognizes authorized users using a trained model
* Identifies unknown persons as intruders
* Captures and saves intruder images
* Sends Telegram alerts along with the captured image
* Triggers a beep sound when an intruder is detected
* Maintains a CSV log of all access events
* Uses confidence averaging for stable predictions
* Includes a cooldown system to avoid repeated alerts


🧠 Technologies Used

* Python
* OpenCV (opencv-contrib-python)
* NumPy
* LBPH Face Recognition
* Haar Cascade for face detection
* Telegram Bot API
* CSV for logging


## 🧩 System Architecture

Webcam Input

      ↓
Face Detection (Haar Cascade)

      ↓
Face Recognition (LBPH Model)

      ↓
Decision Making

   ├── Authorized → No Action
   
   └── Intruder →
   
           ↓
           
      Beep Alarm
      
      Capture Image
      
      Send Telegram Alert
      
      Save Log Entry
      

🔄 How It Works

1. The webcam continuously captures live video
2. Faces are detected using Haar Cascade
3. The system compares the detected face with the trained dataset
4. Based on confidence value, it decides whether the person is authorized

If the person is not recognized:

* A beep alert is triggered
* The image is captured and saved
* A Telegram message is sent with the imag
* The event is recorded in a CSV file


📂 Data Storage

* Intruder images are saved in the `intruder_images/` folder
* All events are recorded in `access_log.csv`
* Alerts are generated using system sound


📷 Output

![Intruder Detection](intruder_2026-03-23_20-19-10.jpg)



📁 Project Structure

project_folder/

│

├── intr.py

├── trainer.yml

├── labels.pkl

├── access_log.csv

│

├── intruder_images/

│

└── dataset/

        └── SUBRAT/
        


🛠️ Installation

bash
pip install opencv-contrib-python numpy requests


▶️ Run

python intr.py

Press 's' to stop.


⚠️ Important Note

Update your Telegram credentials:

bot_token = "YOUR_BOT_TOKEN"
chat_id = "YOUR_CHAT_ID"

🔮 Future Improvements

* Multi-user support
* Raspberry Pi deployment
* Robot integration
* GUI dashboard
* Deep learning upgrade

👨‍💻 Author
   Subrat

⭐ About

A real-time AI surveillance system for detecting and alerting intruders using computer vision.
