from shared.event_store import append_event
import os
import httpx
from fastapi import FastAPI

app = FastAPI(title="MOSI Signal Service", version="1.0.0")
ML_URL = os.getenv("ML_URL", "http://localhost:8010")


@app.get("/health")
def health():
    return {"status": "ok", "service": "signal"}


@app.post("/signals/generate")
def generate_signal(symbol: str = "TCS", user_id: str = "demo-user"):
    features = {
        "pe_ratio": 24.2,
        "debt_to_equity": 0.11,
        "roe": 0.32,
        "volume_trend": 0.73,
        "volatility_30d": 0.18,
    }
    with httpx.Client(timeout=10.0) as client:
        prediction = client.post(f"{ML_URL}/predict", json=features).json()
        explanation = client.post(f"{ML_URL}/explain", json=features).json()

    payload = {
        "user_id": user_id,
        "symbol": symbol,
        "signal": prediction["signal"],
        "confidence": prediction["confidence"],
        "explanation": explanation,
    }
    append_event("predictions", "signal_generated", payload)
    return payload
