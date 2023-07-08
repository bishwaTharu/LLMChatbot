import streamlit as st
import time
from client.chat import prompt
from utils.tts import Hear
from utils.stt import Speaker

# CSS styling for the title
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 36px;
        margin-bottom: 30px;
        color: #325d88;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="title">LLM Chatbot</p>', unsafe_allow_html=True)

if st.button("Ask Me Anything",type='primary'):
    my_text = Hear()
    if my_text:
        st.text_input('Prompt', f'{my_text}')
        chatbot_response = prompt(my_text)
        st.text_area('Chatbot Response', chatbot_response)
        Speaker(chatbot_response)
    else:
        st.text_input('Chatbot Response', "Please first make a prompt")
