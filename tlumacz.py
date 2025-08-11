import sys
import requests
import json
import pyperclip

address="http://localhost:11434/api/generate"
text = pyperclip.paste()
languages = {
    "de": "jobautomation/openeurollm-german:latest",
    "en": "llama3:latest",
    "pl": "jobautomation/openeurollm-polish:latest"
}

if len(sys.argv) == 3 :
    from_language = sys.argv[1]
    to_language = sys.argv[2]
else:
    print("podaj 2 argumenty")
    sys.exit()
    
languages_keys = (sys.argv[2])

if languages_keys not in languages:
    print("Nieobsługiwana para języków.")
    sys.exit()

if languages_keys in languages:
    model=languages[languages_keys]

playload = {
    "model":model,
    "prompt":f''' "You are a professional translator. I will provide the text, source language, and target language. Translate accurately, preserving the meaning, style, and context of the original. Do not add explanations or comments—provide only the translated text. TEXT: '{text}', TARGET LANGUAGE: '{to_language}', SOURCE LANGUAGE: '{from_language}'" ''',
    "stream":False
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(address, data=json.dumps(playload))

try:
    data = response.json()
    print(data.get("response"))
except json.JSONDecodeError:
    print("Błąd")
    print(response.text)
    
    
#python tlumacz.py {j.źródłowy} {j.docelowy} 