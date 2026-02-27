import os
from fastapi import FastAPI

app = FastAPI(title="MOSI Broker Service", version="1.0.0")


@app.get("/health")
def health():
    return {"status": "ok", "service": "broker"}


@app.get("/broker/zerodha/oauth-url")
def get_oauth_url():
    api_key = os.getenv("ZERODHA_API_KEY", "kite_demo_key")
    redirect = os.getenv("ZERODHA_REDIRECT", "http://localhost:8000/callback")
    url = f"https://kite.zerodha.com/connect/login?api_key={api_key}&v=3&redirect_params={redirect}"
    return {"provider": "zerodha", "oauth_url": url}


@app.post("/broker/zerodha/exchange-token")
def exchange_token(request_token: str):
    # Example pykiteconnect usage (stubbed for local development)
    return {
        "provider": "zerodha",
        "request_token": request_token,
        "access_token": "kite_access_token_sample",
        "note": "Replace with KiteConnect(api_key).generate_session in production",
    }


@app.post("/broker/link")
def link_broker(provider: str = "zerodha"):
    return {"linked": True, "provider": provider, "account_id": "Z12345"}
