from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import joblib
import re

# Charger le modèle et le vectorizer
model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/tfidf.pkl")

# Fonction de nettoyage (comme celle utilisée pour l'entraînement)
def clean_text(text):
    text = text.lower()
    text = re.sub(r"\W", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

app = FastAPI()

# Pour servir fichiers statiques (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Page HTML principale
@app.get("/", response_class=HTMLResponse)
async def home():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

# Endpoint pour prédiction
@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    text = data.get("text", "")
    text_clean = clean_text(text)
    vect_text = vectorizer.transform([text_clean])
    pred = model.predict(vect_text)[0]
    label = "True News ✅" if pred == 1 else "Fake News ❌"
    return {"prediction": label}
