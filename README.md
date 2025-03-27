## **🗣️ Simple Voice Assistant in Python**  

**Description:** A lightweight Python-based voice assistant that recognizes speech, responds with text-to-speech, and executes basic commands like searching the web, checking the time, and fetching Wikipedia summaries.  

---

## **Features**  
✔️ **Speech Recognition** – Uses Google Speech API for accurate voice recognition  
✔️ **Text-to-Speech (TTS)** – Converts text responses to speech using `pyttsx3`  
✔️ **Web Search** – Searches Google for queries like “search machine learning”  
✔️ **Wikipedia Lookup** – Retrieves short summaries from Wikipedia  
✔️ **Quick Commands** – Open YouTube, Google, and check the current time  
✔️ **Voice Recordings Storage** – Saves recognized speech as `.wav` files for reference  
✔️ **Modular Codebase** – Well-structured for easy modifications and future upgrades  

---

## **📌 Future Scope**  
**Custom Hotword Activation** – Implement wake-word detection (e.g., “Hey Assistant”)  
**Weather Updates** – Integrate weather forecasts via APIs  
**Email & Messaging** – Add voice-based email & message sending  
**GUI Interface** – Create a simple graphical user interface  

---

## **📂 Project Structure**  
```
voice_assistant/
│── main.py              # Main script  
│── recordings/          # Stores all recorded voice commands  
│   ├── (audio files saved here)  
│── modules/  
│   ├── speech.py        # Handles speech recognition & TTS  
│   ├── commands.py      # Processes voice commands  
│── README.md            # Project documentation  
```

---

## **Getting Started**  

### **1️⃣ Install Dependencies**  
Make sure you have Python 3 installed. Then, install the required packages:  
```bash
pip install speechrecognition pyttsx3 wikipedia
```

### **2️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-username/voice-assistant.git
cd voice-assistant
```

### **3️⃣ Run the Assistant**  
```bash
python main.py
```

### **4️⃣ Give Voice Commands!**  
Here are some examples of what you can say:  
**"What time is it?"** – Tells the current time  
**"Search Python tutorials"** – Opens Google search for the query  
**"Wikipedia Elon Musk"** – Reads a short Wikipedia summary  
**"Open YouTube"** – Opens YouTube in a browser  

---

## **🛠 Troubleshooting**  
🔹 **"Could not connect to speech recognition service"** – Check internet connection  
🔹 **"Sorry, I didn’t catch that"** – Speak clearly and minimize background noise  
🔹 **Recording not saving?** – Ensure the `recordings/` folder exists  

---

## **Contributing**  
Have an idea? Feel free to contribute! Fork this repo, make improvements, and submit a pull request.  

---

## **License**  
This project is open-source—modify and use it as you like! 
