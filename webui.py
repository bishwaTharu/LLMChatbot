import streamlit as st
import time
from client.chat import prompt
from utils.tts import get_speech_input
from utils.stt import Speaker


st.title('LLM Chatbot')
if st.button("Generate"):
    my_text = get_speech_input()
    if my_text:
        st.text_input('Input Field', f'{my_text}')
        chatbot_response = prompt(my_text)
        st.text_input('Chatbot Response', chatbot_response)
        # st.write(title)
        Speaker(chatbot_response)

    else:
        title = st.text_input('Chatbot Response', "Please First make a prompt")

