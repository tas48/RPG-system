from pydantic import BaseModel, Field
from firebase.connection import get_db
import bcrypt

db = get_db()

class User(BaseModel):
    name: str
    password: str

    def hash_password(self):
        self.password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

def check_user_exists(name: str) -> bool:
    user_ref = db.collection("users").document(name)
    doc = user_ref.get()
    return doc.exists  

def create_user(user: User):
    if check_user_exists(user.name):
        return {"message": "User already exists!"}  
    
    user.hash_password()
    user_ref = db.collection("users").document(user.name)
    user_ref.set(user.dict())
    return {"message": "User created successfully!"}

def create_test_user():
    test_user = User(name="Teste Usuário", password="teste123")
    return create_user(test_user)

def get_user(name: str):
    user_ref = db.collection("users").document(name)
    doc = user_ref.get()
    if doc.exists:
        user_data = doc.to_dict()
        return user_data
    else:
        return {"message": "User not found"}

def validate_user(name: str, password: str):
    user_ref = db.collection("users").document(name)
    doc = user_ref.get()
    if doc.exists:
        user_data = doc.to_dict()
        stored_password = user_data.get("password")
        user = User(name=name, password=stored_password)
        if user.check_password(password):
            return {"message": "Login successful!"}
        else:
            return {"message": "Invalid password"}
    else:
        return {"message": "User not found"}
