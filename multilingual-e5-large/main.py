from sentence_transformers import SentenceTransformer
model = SentenceTransformer('intfloat/multilingual-e5-large')

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world(request: str):
    return model.encode(['quiery: ' + request])[0].tolist()