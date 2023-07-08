import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def Speaker(text):
   speaker.Speak(text)