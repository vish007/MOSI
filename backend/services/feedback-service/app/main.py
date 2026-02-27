from shared.event_store import append_event
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="MOSI Feedback Service", version="1.0.0")
EVENTS: list[dict] = []


class Feedback(BaseModel):
    user_id: str
    symbol: str
    signal_id: str
    rating: str
    comment: str | None = None


@app.get("/health")
def health():
    return {"status": "ok", "service": "feedback"}


@app.post("/feedback")
def submit_feedback(payload: Feedback):
    event = payload.model_dump()
    EVENTS.append(event)
    append_event("feedback", "user_feedback", event)
    return {"stored": True, "event": event, "event_count": len(EVENTS)}
