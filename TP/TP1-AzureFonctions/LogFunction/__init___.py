import logging
import json
import os
import azure.functions as func
from azure.storage.blob import BlobServiceClient

# Connexion au compte de stockage Azure via la variable d'environnement
blob_service_client = BlobServiceClient.from_connection_string(os.environ['AzureWebJobsStorage'])

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing log request.')

    try:
        log_data = req.get_json()
    except ValueError:
        return func.HttpResponse(
            "Invalid request body",
            status_code=400
        )

    # Choisir le conteneur pour les logs d'erreurs ou logs généraux
    if log_data.get('level') == 'ERROR':
        container_name = 'error-logs'
    else:
        container_name = 'logs'

    # Récupérer le client du conteneur Blob
    container_client = blob_service_client.get_container_client(container_name)

    # Nom du fichier blob, unique par utilisateur et type de log
    blob_name = f'logs-{log_data.get("user_id")}-{log_data.get("level")}.txt'
    blob_client = container_client.get_blob_client(blob_name)

    # Si le blob n'existe pas, créer un AppendBlob
    if not blob_client.exists():
        blob_client.create_append_blob()

    # Ajouter le log au fichier blob en mode append
    blob_content = json.dumps(log_data) + "\n"
    blob_client.append_block(blob_content)

    return func.HttpResponse(f"Log has been stored in {container_name}", status_code=200)
