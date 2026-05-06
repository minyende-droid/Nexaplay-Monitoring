# NexaPlay Monitoring Runbook

## Alert: ServiceDown

### Meaning

The FastAPI application is unreachable.

### Detection

Prometheus detects:
up{job="nexaplay-app"} == 0

### Investigation Steps

1. Open Grafana dashboard
2. Check application uptime panel
3. Verify container status:
   docker compose ps

### Resolution

Restart the application:
docker compose start app

---

## Alert: HighErrorRate

### Meaning

Application error rate exceeded 5%.

### Investigation Steps

1. Check Error Rate panel in Grafana
2. Inspect recent traffic spikes
3. Identify failing endpoint

### Resolution

Restart service or fix faulty endpoint
