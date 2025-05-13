from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import joblib

app = FastAPI()

# CORS for frontend (React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://sentiment-analysis-frontend-khaki.vercel.app/"],  # For dev use only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model
class InputText(BaseModel):
    text: str

# Load vectorizer and model (assumed pre-trained)
vectorizer = joblib.load("vectorizer.pkl")
model = joblib.load("model.pkl")

@app.post("/predict/")
def predict_emotion(data: InputText):
    vec = vectorizer.transform([data.text])
    pred = model.predict(vec)[0]
    return {"prediction": int(pred)}
