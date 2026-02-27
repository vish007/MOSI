from pathlib import Path
import joblib
import pandas as pd
import shap
from fastapi import FastAPI
from pydantic import BaseModel

MODEL_FILE = Path(__file__).resolve().parent.parent / "model" / "mosi_xgb.joblib"
payload = joblib.load(MODEL_FILE)
model = payload["model"]
features = payload["features"]
explainer = shap.TreeExplainer(model)

app = FastAPI(title="MOSI ML Service", version="1.0.0")


class FeatureInput(BaseModel):
    pe_ratio: float
    debt_to_equity: float
    roe: float
    volume_trend: float
    volatility_30d: float


@app.get("/health")
def health():
    return {"status": "ok", "service": "ml"}


@app.post("/train")
def train():
    from model.train import train_and_save

    train_and_save()
    return {"trained": True}


@app.post("/predict")
def predict(data: FeatureInput):
    df = pd.DataFrame([data.model_dump()])[features]
    prob = float(model.predict_proba(df)[0][1])
    return {
        "signal": "BUY" if prob > 0.5 else "HOLD/AVOID",
        "confidence": round(prob, 4),
    }


@app.post("/explain")
def explain(data: FeatureInput):
    df = pd.DataFrame([data.model_dump()])[features]
    values = explainer.shap_values(df)
    row = values[0]
    ranked = sorted(zip(features, row), key=lambda x: abs(x[1]), reverse=True)[:5]
    top = [{"feature": f, "impact": float(v)} for f, v in ranked]
    english = "Top drivers: " + ", ".join(
        [f"{item['feature']} ({'positive' if item['impact'] > 0 else 'negative'} impact)" for item in top]
    )
    return {"top_features": top, "english_explanation": english}
