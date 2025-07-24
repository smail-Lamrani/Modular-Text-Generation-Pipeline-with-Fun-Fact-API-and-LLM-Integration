import requests
import os
from datetime import datetime

def ingest():
    os.makedirs("data/raw", exist_ok=True)
    facts = []
    for _ in range(10):
        response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")
        facts.append(response.json()["text"])

    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M")
    file_path = f"data/raw/facts_{timestamp}.txt"
    with open(file_path, "w") as f:
        for fact in facts:
            f.write(fact + "\n")
    return file_path
