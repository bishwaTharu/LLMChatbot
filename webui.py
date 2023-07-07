import streamlit as st
import speech_recognition as sr
import pyttsx3
import time
import win32com.client
from client.chat import prompt

speaker = win32com.client.Dispatch("SAPI.SpVoice")
r = sr.Recognizer()
engine = pyttsx3.init()


def get_speech_input():
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
        
def speak_output(text):
   speaker.Speak(text)


st.title('LLM Chatbot')


if st.button("Generate"):
    my_text = get_speech_input()
    if my_text:
        st.text_input('Input Field', f'{my_text}')
        chatbot_response = prompt(my_text)
        st.text_input('Chatbot Response', chatbot_response)
        # st.write(title)
        speak_output(chatbot_response)

    else:
        title = st.text_input('Chatbot Response', "Please First make a prompt")

