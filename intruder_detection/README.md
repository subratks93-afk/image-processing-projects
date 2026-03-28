🛡️ AI-Based Smart Intruder Detection System
📌 Overview
This project is a real-time surveillance system built using Python and OpenCV. It detects human faces through a webcam and identifies whether the person is authorized or an intruder using face recognition.
If an intruder is detected, the system:
•	Captures the image 📷 
•	Triggers an alert 🔊 
•	Sends a Telegram notification 📩 
•	Logs the event 📊 
________________________________________
🚀 Features
•	Real-time face detection using webcam 
•	Face recognition using trained LBPH model 
•	Authorized vs Intruder classification 
•	Automatic intruder image capture 
•	Telegram alert with image 
•	Audio alert (beep system) 
•	CSV-based logging system 
•	Confidence averaging for stable predictions 
•	Cooldown mechanism to prevent alert spam 
________________________________________
🧠 Technologies Used
•	Python 
•	OpenCV (opencv-contrib-python) 
•	NumPy 
•	LBPH Face Recognition 
•	Haar Cascade (Face Detection) 
•	Telegram Bot API 
•	CSV (Logging system) 
________________________________________
🧩 System Architecture

Webcam Input

      ↓
      
Face Detection (Haar Cascade)

      ↓
      
Face Recognition (LBPH)

      ↓
      
Decision Making

   ├── Authorized → No Action
   
   └── Intruder →
   
           ↓
           
     Beep Alert
     
     Capture Image
     
     Send Telegram Alert
     
     Save Log (CSV)
     
________________________________________
🔄 How It Works
1.	Webcam captures live video 
2.	Faces are detected using Haar Cascade 
3.	Face is compared with trained dataset 
4.	System checks confidence score 
5.	If intruder detected: 
o	Beep alert is triggered 
o	Image is saved 
o	Telegram alert is sent 
o	Event is logged in CSV 
________________________________________
📂 Data Storage
•	📷 Intruder images → intruder_images/ 
•	📊 Logs → access_log.csv 
________________________________________
📁 Project Structure
intruder_system/

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
    
________________________________________
🛠️ Installation
pip install opencv-contrib-python numpy requests
________________________________________
▶️ Run

python intr.py

Press 's' to stop the system.

________________________________________
⚠️ Important Note
Update your Telegram credentials before running:
bot_token = "YOUR_BOT_TOKEN"
chat_id = "YOUR_CHAT_ID"
________________________________________
🔮 Future Improvements
•	Multi-user face recognition 
•	Raspberry Pi deployment 
•	Robot integration 🤖 
•	GUI dashboard 
•	Deep learning-based model (YOLO / CNN) 
________________________________________
👨‍💻 Author
Subrat
________________________________________
⭐ About
A real-time AI surveillance system for detecting and alerting intruders using computer vision.

