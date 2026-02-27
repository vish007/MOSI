from fastapi import FastAPI

app = FastAPI(title="MOSI Auth Service", version="1.0.0")


@app.get("/health")
def health():
    return {"status": "ok", "service": "auth"}


@app.post("/auth/demo-login")
def demo_login():
    return {
        "access_token": "demo-token",
        "user": {"id": "demo-user", "name": "Demo Investor", "risk_profile": "moderate"},
    }
