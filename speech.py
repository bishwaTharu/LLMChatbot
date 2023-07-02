import speech_recognition as sr
import pyttsx3
from api.chat import prompt
# Initialize the recognizer
r = sr.Recognizer()
engine = pyttsx3.init()

def get_speech_input():
    # Use the microphone as the source for input
    with sr.Microphone() as source:
        # Adjust the energy threshold based on surrounding noise level
        r.adjust_for_ambient_noise(source, duration=0.2)

        print("Listening...")

        # Listen for the user's input
        audio = r.listen(source)

        print("Recognizing...")

        # Using Google to recognize audio
        try:
            recognized_text = r.recognize_google(audio)
            recognized_text = recognized_text.lower()
            print("You said:", recognized_text)
            return recognized_text
        except sr.UnknownValueError:
            print("Unable to recognize speech")
            return ""
        except sr.RequestError as e:
            print("Error occurred while requesting speech recognition: {0}".format(e))
            return ""

def speak_output(text):
    # Speak the provided text
    print(f"Response: {text}")
    engine.say(text)
    engine.runAndWait()

# Example usage:
input_text = get_speech_input()
print("processing...")
decoded = prompt(input_text)
speak_output(decoded)

