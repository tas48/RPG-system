from google.cloud import firestore
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar as credenciais do Firebase
firebase_credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = firebase_credentials_path

# Inicializar o cliente do Firestore
db = firestore.Client()

# Definir o modelo de usuário usando Pydantic
class User(BaseModel):
    name: str
    email: str

# Função para criar um usuário no Firestore
def create_user(user: User):
    user_ref = db.collection("users").document(user.email)
    user_ref.set(user.dict())
    return {"message": "User created successfully!"}

# Função para criar um usuário de teste
def create_test_user():
    test_user = User(name="Teste Usuário", email="teste@usuario.com")
    return create_user(test_user)

# Função para recuperar um usuário do Firestore
def get_user(email: str):
    user_ref = db.collection("users").document(email)
    doc = user_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return {"message": "User not found"}
