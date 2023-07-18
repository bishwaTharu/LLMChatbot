import streamlit as st
# from client.chat import prompt
from client.RayServices import distributedChat

from utils.tts import Hear
# import win32com.client
# speaker = win32com.client.Dispatch("SAPI.SpVoice")

# def Speaker(text):
#    speaker.Speak(text)
# from utils.stt import Speaker

st.title("LLM CHATBOT")
if st.button("Ask Me Anything",type='primary'):
    my_text = Hear()
    if my_text:
        st.text_input('Prompt', f'{my_text}')
        chatbot_response = distributedChat(my_text)
        st.text_area('Chatbot Response', chatbot_response)
        # Speaker(chatbot_response)
    else:
        st.text_input('Chatbot Response', "Please first make a prompt")