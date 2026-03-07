import json
import requests
from datetime import datetime

URL = "https://raw.githubusercontent.com/huynhngoc4846/vote-tracker/main/votes.json"

try:
    res = requests.get(URL)
    votes = res.json()
except:
    votes = []

now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

data = {
    "time": now,
    "votes": votes
}

with open("history.json","r") as f:
    history = json.load(f)

history.append(data)

with open("history.json","w") as f:
    json.dump(history,f,indent=2)
