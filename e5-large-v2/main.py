from sentence_transformers import SentenceTransformer
model = SentenceTransformer('intfloat/e5-large-v2')

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world(request: str):
    return model.encode(['quiery: ' + request])[0].tolist()