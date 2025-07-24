import argparse
from datetime import datetime
from ingest import ingest
from prompt_engine import call_model
import os
import cohere
def run_pipeline(real_model: bool = True):
    print(" Lancement du pipeline...")

    # 1. INGESTION : récupération des faits depuis l’API
    print("Récupération des faits amusants...")
    facts_file = ingest()

    with open(facts_file, "r") as f:
        facts = f.readlines()

    # 2. TRANSFORMATION : traitement de chaque fait via l’invite
    print(" Génération des insights...")
    results = []
    for fact in facts:
        fact = fact.strip()
        prompt = f"Explain why this fun fact is interesting to humans: {fact}"
        response = call_model(prompt, real_model=real_model)

        result = f"FACT: {fact}\nPROMPT: {prompt}\nRESPONSE: {response}\n"
        results.append(result)

    # 3. ENREGISTREMENT DES RÉSULTATS
    os.makedirs("data/processed", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M")
    output_path = f"data/processed/facts_output_{timestamp}.txt"

    with open(output_path, "w") as f:
        for line in results:
            f.write(line + "\n")

    print(f" Pipeline terminé. Fichier sauvegardé dans : {output_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run the text processing pipeline.")
    parser.add_argument('--real-model', action='store_true', help="Utiliser le vrai modèle LLM via API Cohere")

    args = parser.parse_args()
    run_pipeline(real_model=args.real_model)
    print(f"[DEBUG] args.real_model = {args.real_model}")

