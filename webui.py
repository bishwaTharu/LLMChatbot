import streamlit as st
from client.chat import prompt
from utils.tts import Hear
from utils.stt import Speaker


if st.button("Ask Me Anything",type='primary'):
    my_text = Hear()
    if my_text:
        st.text_input('Prompt', f'{my_text}')
        chatbot_response = prompt(my_text)
        st.text_area('Chatbot Response', chatbot_response)
        Speaker(chatbot_response)
    else:
        st.text_input('Chatbot Response', "Please first make a prompt")