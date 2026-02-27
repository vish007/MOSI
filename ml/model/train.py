from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from xgboost import XGBClassifier

MODEL_PATH = Path(__file__).resolve().parent / "mosi_xgb.joblib"


def make_data(n: int = 2000):
    rng = np.random.default_rng(42)
    df = pd.DataFrame(
        {
            "pe_ratio": rng.normal(22, 8, n).clip(2, 70),
            "debt_to_equity": rng.normal(0.5, 0.3, n).clip(0, 3),
            "roe": rng.normal(0.18, 0.08, n).clip(0, 0.8),
            "volume_trend": rng.normal(0.0, 1.0, n),
            "volatility_30d": rng.normal(0.22, 0.08, n).clip(0.05, 0.7),
        }
    )
    y = (
        (df["roe"] > 0.2)
        & (df["debt_to_equity"] < 0.7)
        & (df["pe_ratio"] < 30)
        & (df["volatility_30d"] < 0.3)
    ).astype(int)
    return df, y


def train_and_save():
    X, y = make_data()
    model = XGBClassifier(n_estimators=60, max_depth=4, learning_rate=0.08, random_state=42)
    model.fit(X, y)
    payload = {"model": model, "features": list(X.columns), "baseline": X.sample(200, random_state=1)}
    joblib.dump(payload, MODEL_PATH)
    print(f"saved model => {MODEL_PATH}")


if __name__ == "__main__":
    train_and_save()
