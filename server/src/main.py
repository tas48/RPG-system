from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    response = "teste"
    return response
