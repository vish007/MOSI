# mosi-platform

Production-grade monorepo for MOSI (Margin of Safety Intelligence) with:
- **Mobile**: Expo SDK 54 + TypeScript app
- **Backend**: FastAPI microservices with OpenAPI, Gunicorn/Uvicorn, Docker, Kubernetes
- **ML**: Train/predict/explain APIs with SHAP and monitoring hooks
- **Infra/Ops**: docker-compose, Kubernetes manifests, CI/CD, security scans

## Repository Layout

- `mobile/` Expo app for investor experience
- `backend/` FastAPI microservices
- `ml/` model training + inference + explainability
- `infra/` Kubernetes and Helm assets
- `ops/` scripts, seed/demo bootstrap
- `docs/` architecture and API references

## Quickstart (Local, Docker)

```bash
docker compose up --build
```

Services:
- API Gateway: `http://localhost:8000`
- Auth: `http://localhost:8001`
- Broker: `http://localhost:8002`
- Portfolio: `http://localhost:8003`
- Signals: `http://localhost:8004`
- Feedback: `http://localhost:8005`
- ML Service: `http://localhost:8010`
- Postgres: `localhost:5432`

## Demo data

Create seeded demo tenant/user and synthetic portfolio/signal data:

```bash
./ops/scripts/demo.sh
```

## End-to-End Flow Covered

1. User links broker (Zerodha OAuth sample)
2. Portfolio sync creates holdings snapshot
3. Signal service fetches ML prediction + SHAP explanation
4. Mobile displays signal card + explanation text
5. User feedback API records thumbs up/down and stores events
6. Monitoring pipeline can emit alert webhook for dashboard ingestion

## Kubernetes deploy

```bash
kubectl apply -f infra/k8s/namespace.yaml
kubectl apply -f infra/k8s/postgres.yaml
kubectl apply -f infra/k8s/ml-service.yaml
kubectl apply -f infra/k8s/backend-services.yaml
```

## CI

GitHub Actions workflow (`.github/workflows/ci.yml`) runs:
- lint
- unit tests
- Docker image builds
- Trivy security scan
- optional push to registry (on main)

## Notes

- The provided feature PDF path was unavailable in this environment, so screens were implemented from the explicit MOSI flow/features provided in the prompt.
