import requests
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset


def check_drift(reference_df, current_df, webhook_url: str):
    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=reference_df, current_data=current_df)
    result = report.as_dict()
    drift = result["metrics"][0]["result"].get("dataset_drift", False)
    if drift:
        requests.post(webhook_url, json={"type": "MODEL_DRIFT", "payload": result}, timeout=5)
    return {"drift_detected": drift}
