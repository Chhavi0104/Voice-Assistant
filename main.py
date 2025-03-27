from modules.speech import recognize_speech, speak
from modules.commands import process_command
import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia
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

def process_command(command):
    """Process the recognized command and execute appropriate actions"""
    if command is None:
        return
    
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
    
    elif "search" in command:
        query = command.replace("search", "").strip()
        speak(f"Searching for {query} on Google")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    
    elif "wikipedia" in command:
        query = command.replace("wikipedia", "").strip()
        speak(f"Searching Wikipedia for {query}")
        try:
            summary = wikipedia.summary(query, sentences=2)
            speak(summary)
        except wikipedia.exceptions.DisambiguationError:
            speak("There are multiple results. Please be more specific.")
        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find anything on Wikipedia.")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I didn't understand that command.")

# Main loop
if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I help you?")
    while True:
        user_command = recognize_speech()
        process_command(user_command)

if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I help you?")
    while True:
        user_command = recognize_speech()
        process_command(user_command)
