from google.cloud import firestore
import os
from dotenv import load_dotenv

load_dotenv()

firebase_credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = firebase_credentials_path

# Inicializar o cliente do Firestore
db = firestore.Client()

# Função para obter o cliente de conexão
def get_db():
    return db
