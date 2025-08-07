import sys
import requests
import json
import pyperclip

address="http://localhost:11434/api/generate"
text = pyperclip.paste()
languages = {
    ("pl", "de"): "qwen2.5:latest",
    ("pl", "en"): "qwen2.5:latest",
    ("de", "pl"): "qwen2.5:latest",
    ("de", "en"): "qwen2.5:latest",
    ("en", "de"): "qwen2.5:latest",
    ("en", "pl"): "qwen2.5:latest",
}

if len(sys.argv) == 3 :
    from_language = sys.argv[1]
    to_language = sys.argv[2]
else:
    print("podaj 2 argumenty")
    sys.exit()
    
languages_keys = (sys.argv[1], sys.argv[2])

if languages_keys not in languages:
    print("Nieobsługiwana para języków.")
    sys.exit()

if languages_keys in languages:
    model=languages[languages_keys]

playload = {
    "model":model,
    "prompt":f''' "Jesteś profesjonalnym tłumaczem. Podam tekst, język źródłowy i docelowy. Tłumacz dokładnie, zachowując sens, styl i kontekst oryginału. Nie dodawaj wyjaśnień ani komentarzy — podaj wyłącznie przetłumaczony tekst. TEKST: '{text}', JĘZYK DOCELOWY: '{to_language}', JĘZYK ŹRÓDŁOWY: '{from_language}'" ''',
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