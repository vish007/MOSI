import os
import httpx
from fastapi import FastAPI

app = FastAPI(title="MOSI API Gateway", version="1.0.0")
AUTH_URL = os.getenv("AUTH_URL", "http://localhost:8001")
BROKER_URL = os.getenv("BROKER_URL", "http://localhost:8002")
PORTFOLIO_URL = os.getenv("PORTFOLIO_URL", "http://localhost:8003")
SIGNAL_URL = os.getenv("SIGNAL_URL", "http://localhost:8004")
FEEDBACK_URL = os.getenv("FEEDBACK_URL", "http://localhost:8005")

ALERTS: list[dict] = []


@app.get("/health")
def health():
    return {"status": "ok", "service": "gateway"}


@app.post("/flow/demo")
def run_demo_flow():
    with httpx.Client(timeout=15.0) as client:
        login = client.post(f"{AUTH_URL}/auth/demo-login").json()
        broker = client.post(f"{BROKER_URL}/broker/link", params={"provider": "zerodha"}).json()
        portfolio = client.post(f"{PORTFOLIO_URL}/portfolio/sync", params={"user_id": login['user']['id']}).json()
        signal = client.post(f"{SIGNAL_URL}/signals/generate", params={"symbol": "TCS", "user_id": login['user']['id']}).json()

    return {"login": login, "broker": broker, "portfolio": portfolio, "signal": signal}


@app.post("/feedback")
def proxy_feedback(payload: dict):
    with httpx.Client(timeout=10.0) as client:
        return client.post(f"{FEEDBACK_URL}/feedback", json=payload).json()


@app.post("/admin/alerts/webhook")
def monitoring_alert(payload: dict):
    ALERTS.append(payload)
    return {"received": True, "count": len(ALERTS)}
