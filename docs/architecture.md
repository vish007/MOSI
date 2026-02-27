# MOSI Platform Architecture

- Mobile app calls API Gateway for a single orchestration endpoint.
- Gateway composes Auth, Broker, Portfolio, Signal, and Feedback services.
- Signal service calls ML prediction + SHAP explain endpoints.
- Feedback events and prediction telemetry are appended to event store and persisted in Postgres schema.
- Monitoring (Evidently) posts drift alerts to admin dashboard webhook.
