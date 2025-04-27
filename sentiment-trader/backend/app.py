import streamlit as st
from fastapi import FastAPI
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = FastAPI()

model = AutoModelForSequenceClassification.from_pretrained("your/memebert")
tokenizer = AutoTokenizer.from_pretrained("your/memebert")

@app.post("/predict_sentiment")
def predict(text: str):
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs).logits
    score = torch.softmax(outputs, dim=1)[0][1].item()
    return {"score": score}
