from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis", 'blanchefort/rubert-base-cased-sentiment')


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    """Predict tone detection"""
    return classifier(item.text)[0]
