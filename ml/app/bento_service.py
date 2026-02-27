import bentoml

# Example BentoML wrapper around the trained model artifact
mosi_runner = bentoml.xgboost.get("mosi_xgb:latest").to_runner()
svc = bentoml.Service("mosi_signal", runners=[mosi_runner])


@svc.api(input=bentoml.io.JSON(), output=bentoml.io.JSON())
def predict(payload):
    return mosi_runner.predict.run(payload)
