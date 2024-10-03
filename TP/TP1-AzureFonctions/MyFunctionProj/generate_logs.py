import json
import time
import random
import requests

sample_logs = [
    {"level": "INFO", "message": "User logged in", "user_id": 1},
    {"level": "DEBUG", "message": "Query executed", "user_id": 3},
    {"level": "INFO", "message": "Data exported successfully", "user_id": 5},
]

error_logs = [
    {"level": "ERROR", "message": "Failed to connect to database", "user_id": 2},
    {"level": "ERROR", "message": "Permission denied", "user_id": 4},
]

CLOUD_FUNCTION_ENDPOINT = "https://tp1logfuction.azurewebsites.net/logfunction" 
def send_log_to_cloud_function(log):
    try:
        response = requests.post(CLOUD_FUNCTION_ENDPOINT, json=log)
        if response.status_code == 200:
            print(f"Sent log: {log}")
        else:
            print(f"Failed to send log: {log}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending log: {e}")

def simulate_log_stream():
    while True:
        # Générer un log aléatoire (90% d'infos, 10% d'erreurs)
        if random.random() < 0.1:
            log = random.choice(error_logs)
        else:
            log = random.choice(sample_logs)

        # Envoyer le log à la fonction Azure
        send_log_to_cloud_function(log)

        # Attendre un temps aléatoire entre 1 et 3 secondes
        time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    simulate_log_stream()
