from fastapi import FastAPI
from model import create_user, get_user, User, create_test_user

app = FastAPI()

# Rota principal que cria o usuário de teste
@app.get("/")
def root():
    response = create_test_user()
    return response
