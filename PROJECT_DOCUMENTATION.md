# Enterprise LLM Security Gateway

## Overview

The Enterprise LLM Security Gateway is a FastAPI-based security layer that sits between enterprise users and Large Language Models (LLMs).

The gateway provides:

* Authentication
* Role-Based Access Control (RBAC)
* Rate Limiting
* PII Detection and Redaction
* Prompt Injection Detection
* SQL Injection Detection
* Audit Logging
* Security Dashboard
* Docker Deployment

## Technology Stack

* Python
* FastAPI
* PostgreSQL
* Microsoft Presidio
* Docker
* GitHub

## Security Features

### Authentication

Validates enterprise users before allowing access.

### RBAC

Restricts model access based on user role.

### Data Loss Prevention (DLP)

Detects and redacts:

* Names
* Emails
* Credit Cards
* Employee IDs
* Internal Project Codes

### Prompt Injection Protection

Blocks prompts attempting to override system instructions.

### SQL Injection Protection

Blocks malicious SQL payloads.

### Audit Logging

Stores all requests in PostgreSQL.

### Security Dashboard

Provides request statistics and security metrics.

## Deployment

Application is containerized using Docker and exposed on port 8000.
