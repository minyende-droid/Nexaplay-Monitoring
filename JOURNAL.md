# JOURNAL.md

## Week 1

### Day 1 — Project Setup and Environment Preparation

Today I reviewed the NexaPlay project requirements and understood the purpose of the monitoring stack. I learned the roles of Prometheus, Grafana, Alertmanager, Node Exporter, and Docker Compose. Because Docker Desktop and virtualization were not supported on my laptop, I switched to GitHub Codespaces as my development environment. I cloned the repository, explored the folder structure, and verified Docker and Docker Compose were working inside Codespaces.

---

### Day 2 — Containerising the FastAPI Application

Today I learned how containerisation works using Docker. I reviewed the FastAPI application structure and created a Dockerfile for the NexaPlay game server application. I built the Docker image and tested the container locally in Codespaces. I then connected the application to Docker Compose and verified the app was accessible through the forwarded Codespaces port.

---

### Day 3 — Prometheus Configuration and Metrics Collection

Today I configured Prometheus to scrape metrics from both the FastAPI application and Node Exporter. I edited the `prometheus.yml` file and verified that Prometheus targets were successfully being scraped. I explored the `/metrics` endpoint exposed by the FastAPI app and learned how Prometheus stores time-series metrics data.

---

### Day 4 — Grafana Dashboard Creation

Today I configured Grafana and connected it to Prometheus as a data source. I created a monitoring dashboard with panels showing active players, request rate, error rate, and CPU usage. I learned how PromQL queries work and how Grafana visualizes metrics data. After completing the dashboard, I exported it as a JSON file and saved it into the project repository.

---

### Day 5 — Alerting System Setup

Today I configured alert rules in Prometheus for `ServiceDown` and `HighErrorRate`. I learned how Prometheus alert expressions work and how alert conditions are evaluated over time. I then configured Alertmanager to send notifications through Gmail using SMTP authentication and App Passwords. After testing the alerts by stopping the application container, I successfully received alert notifications in my Gmail inbox.

---

## Week 2

### Day 6 — Alert Testing and Incident Simulation

Today I tested the monitoring stack under failure conditions. I simulated service outages and verified that Prometheus, Alertmanager, and Grafana worked together correctly. I practiced stopping and restarting containers and observed how alerts changed from firing to resolved. This helped me understand the full alert lifecycle.

---

### Day 7 — Incident Investigation Using Grafana and Prometheus

Today I triggered the built-in incident scenario and investigated it using Grafana dashboards and Prometheus metrics instead of reading raw logs. I analyzed spikes in request errors and system behavior through visual graphs. I learned how dashboards help engineers quickly identify where problems are occurring during incidents.

---

### Day 8 — AWS S3 Integration

Today I created an AWS S3 bucket and configured an IAM user with limited permissions for secure access. I wrote the `export_to_s3.py` script using boto3 to upload the Grafana dashboard JSON backup into the S3 bucket. After running the script successfully, I verified that the dashboard file appeared in the bucket.

---

### Day 9 — GitHub Actions and Project Cleanup

Today I created a GitHub Actions workflow to validate the Docker Compose and Prometheus configuration files automatically on every push to the repository. I tested the workflow and confirmed that the checks passed successfully. I also organized the repository structure and reviewed all project files to ensure everything matched the required deliverables.

---

### Day 10 — Documentation and Final Review

Today I completed the project documentation, including the runbook and incident report. I reviewed the complete monitoring stack and practiced explaining how Prometheus, Grafana, Alertmanager, and Node Exporter work together. I also reviewed the original NexaPlay outage scenario and reflected on how the monitoring system would have reduced the incident response time significantly.
