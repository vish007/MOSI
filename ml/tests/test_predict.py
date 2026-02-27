from fastapi.testclient import TestClient
from app.main import app


def test_predict_endpoint():
    client = TestClient(app)
    res = client.post('/predict', json={
        'pe_ratio': 20,
        'debt_to_equity': 0.3,
        'roe': 0.25,
        'volume_trend': 0.2,
        'volatility_30d': 0.2
    })
    assert res.status_code == 200
    assert 'signal' in res.json()
