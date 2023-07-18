import requests
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
SERVER_IP = os.getenv("BASE_URL")

def distributedChat(prompt:str)->str:
    response_ref = requests.post(f"{SERVER_IP}/?text={prompt}")
    response = response_ref.content.decode()
    return response
