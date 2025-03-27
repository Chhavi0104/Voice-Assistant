import os
import speech_recognition as sr
import pyttsx3
import datetime
import wave

# Ensure recordings directory exists
RECORDINGS_DIR = "recordings"
os.makedirs(RECORDINGS_DIR, exist_ok=True)

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Adjust speaking speed

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    """Recognize speech from microphone and save recording"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        try:
            audio = recognizer.listen(source, timeout=5)

            # Save recording
            file_path = os.path.join(RECORDINGS_DIR, f"command_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.wav")
            with wave.open(file_path, "wb") as file:
                file.setnchannels(1)
                file.setsampwidth(2)
                file.setframerate(16000)
                file.writeframes(audio.get_wav_data())

            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            print("Could not connect to speech recognition service.")
            return None
