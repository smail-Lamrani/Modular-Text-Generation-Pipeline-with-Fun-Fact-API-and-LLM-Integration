import cohere
from ingest import ingest
import os 
API_KEY = "put-the_api_key_of_cohere"

def call_model(prompt: str, real_model: bool = True) -> str:
    if real_model and API_KEY:
        co = cohere.Client(API_KEY)
        try:
            response = co.generate(
                prompt=prompt,
                max_tokens=50
                )
            return response.generations[0].text.strip()
        except Exception as e:
            return f"[ERROR from Cohere] {e}"
    else:
        return f"[SIMULATED INSIGHT] {prompt}"
       

    #pour tester
from prompt_engine import call_model

fact = "Bananas are berries, but strawberries are not."
prompt = f"Explain why this fun fact is interesting to humans: {fact}"

# Test en mode simulation
response = call_model(prompt)
print(" Mode Simulation:")
print(response)
