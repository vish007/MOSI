from fastapi import FastAPI

app = FastAPI(title="MOSI Portfolio Service", version="1.0.0")


@app.get("/health")
def health():
    return {"status": "ok", "service": "portfolio"}


@app.post("/portfolio/sync")
def sync_portfolio(user_id: str = "demo-user"):
    holdings = [
        {"symbol": "TCS", "qty": 10, "avg_price": 3500, "sector": "IT"},
        {"symbol": "HDFCBANK", "qty": 5, "avg_price": 1600, "sector": "BANKING"},
    ]
    return {"user_id": user_id, "synced": True, "holdings": holdings}
