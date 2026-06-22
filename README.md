## Enterprise LLM Security Gateway

The Enterprise LLM Security Gateway is a security-focused middleware application built using FastAPI and Python. It acts as a protective layer between enterprise users and Large Language Models (LLMs), ensuring that requests are validated, monitored, and secured before reaching the AI system.

The gateway includes user authentication, role-based access control (RBAC), rate limiting, PII detection and redaction using Microsoft Presidio, prompt injection detection, SQL injection protection, and PostgreSQL-based audit logging. It also provides a security dashboard for monitoring request activity and security events.

To support modern deployment practices, the application has been containerized using Docker and configured for Kubernetes deployment with Horizontal Pod Autoscaling (HPA).

### Technologies Used

* Python
* FastAPI
* PostgreSQL
* Microsoft Presidio
* Docker
* Kubernetes
* Git & GitHub

### Key Features

* Authentication and RBAC
* Data Loss Prevention (DLP)
* PII Detection and Redaction
* Prompt Injection Protection
* SQL Injection Detection
* Audit Logging
* Security Dashboard
* Dockerized Deployment
* Kubernetes & HPA Configuration
