🛡️ AI-Based Smart Intruder Detection System
________________________________________
📌 Overview
This project is a real-time surveillance system built using Python and OpenCV. The main idea behind the project is to detect a person through a webcam and check whether they are authorized or not using face recognition.
If an unknown person appears in front of the camera, the system automatically captures their image, triggers a beep alert, sends a notification via Telegram, and stores the event in a log file for future reference.
________________________________________
🚀 Features
•	Detects faces in real-time using a webcam
•	Recognizes authorized users using a trained model
•	Identifies unknown persons as intruders
•	Captures and saves intruder images
•	Sends Telegram alerts along with the captured image
•	Triggers a beep sound when an intruder is detected
•	Maintains a CSV log of all access events
•	Uses confidence averaging for more stable predictions
•	Includes a cooldown system to avoid repeated alerts
________________________________________
🧠 Technologies Used
•	Python
•	OpenCV (opencv-contrib-python)
•	NumPy
•	LBPH Face Recognition
•	Haar Cascade for face detection
•	Telegram Bot API
•	CSV for logging
________________________________________
🧩 System Architecture
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
________________________________________
🔄 How It Works
1.	The webcam continuously captures live video
2.	Faces are detected using Haar Cascade
3.	The system compares the detected face with the trained dataset
4.	Based on confidence value, it decides whether the person is authorized
5.	If the person is not recognized:
o	A beep alert is triggered
o	The image is captured and saved
o	A Telegram message is sent with the image
o	The event is recorded in a CSV file
________________________________________
📂 Data Storage
•	Intruder images are saved in the intruder_images/ folder
•	All events are recorded in access_log.csv
•	Alerts are generated using system sound
________________________________________
📷 Output
 
________________________________________
📁 Project Structure
project_folder/
│
├── intr.py                  # Main detection program
├── trainer.yml              # Trained model
├── labels.pkl               # Label mapping
├── access_log.csv           # Log file
│
├── intruder_images/         # Stored intruder images
│
└── dataset/
        └── SUBRAT/          # Authorized user images
________________________________________
🛠️ Installation
pip install opencv-contrib-python numpy requests
________________________________________
▶️ Running the Project
python intr.py
Press 's' to stop the system.
________________________________________
⚠️ Important Note
Before running the project, make sure to update your Telegram bot details in the code:
bot_token = "YOUR_BOT_TOKEN"
chat_id = "YOUR_CHAT_ID"
Avoid sharing your bot token publicly for security reasons.
________________________________________
🔮 Future Improvements
•	Support for multiple authorized users
•	Deployment on Raspberry Pi
•	Integration with mobile robots
•	Adding a GUI dashboard
•	Using deep learning models for better accuracy
________________________________________
👨‍💻 Author
Subrat
AI & Robotics Enthusiast
________________________________________
⭐ About This Project
This project was developed to explore how computer vision can be used for real-time monitoring and security systems. It demonstrates a complete pipeline from detection to decision-making and automated alerting.

