import pyttsx3
import speech_recognition as sr
import streamlit as st
r = sr.Recognizer()

def Hear():
    # Use the microphone as the source for input
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        st.info("Listening...")
        audio = r.listen(source)
        try:
            recognized_text = r.recognize_google(audio)
            recognized_text = recognized_text.lower()
            st.info("Recognized...")
            return recognized_text
        except sr.UnknownValueError:
            print("Unable to recognize speech")
            return ""
        except sr.RequestError as e:
            print("Error occurred while requesting speech recognition: {0}".format(e))
            return ""