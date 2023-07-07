import requests
import json
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
SERVER_IP = os.getenv("BASE_URL")

URL = f"{SERVER_IP}/api/v1/generate"


def prompt(inp):
    data = {"text": inp}
    headers = {'Content-type': 'application/json'}

    response = requests.post(URL, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        return response.json()["generated_text"][0]["generated_text"]
    else:
        return "Error:", response.status_code
    
