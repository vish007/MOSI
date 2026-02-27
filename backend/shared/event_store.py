"""Simple event store abstraction for replay-ready telemetry."""
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Any


@dataclass
class Event:
    stream: str
    event_type: str
    payload: dict[str, Any]
    created_at: str = datetime.utcnow().isoformat()


EVENT_LOG: list[dict[str, Any]] = []


def append_event(stream: str, event_type: str, payload: dict[str, Any]) -> dict[str, Any]:
    event = Event(stream=stream, event_type=event_type, payload=payload)
    data = asdict(event)
    EVENT_LOG.append(data)
    return data


def replay(stream: str) -> list[dict[str, Any]]:
    return [e for e in EVENT_LOG if e["stream"] == stream]
