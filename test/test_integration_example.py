import sys
import os

# Cette ligne dit à Python de regarder aussi dans le dossier parent pour trouver 'app'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.app import app

def test_health_endpoint():
    # On utilise le client de test de Flask
    client = app.test_client()
    # On simule une requête GET sur l'URL racine
    response = client.get("/")
    # On vérifie que le serveur répond avec un code 200 (Succès)
    assert response.status_code == 200