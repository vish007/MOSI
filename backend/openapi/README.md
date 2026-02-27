# OpenAPI Specs

Run each service and retrieve:

```bash
curl http://localhost:8001/openapi.json > auth-service.json
curl http://localhost:8002/openapi.json > broker-service.json
curl http://localhost:8003/openapi.json > portfolio-service.json
curl http://localhost:8004/openapi.json > signal-service.json
curl http://localhost:8005/openapi.json > feedback-service.json
curl http://localhost:8000/openapi.json > api-gateway.json
```

Example endpoint groups are implemented in each service `app/main.py`.
