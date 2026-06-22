from fastapi import FastAPI, HTTPException

from models.request_model import ChatRequest

from services.auth_service import authenticate_user
from services.rate_limit_service import check_rate_limit
from services.db_log_service import save_log
from services.dlp_service import sanitize_prompt
from services.prompt_injection_service import detect_prompt_injection
from services.sql_injection_service import detect_sql_injection
from services.dashboard_service import get_audit_statistics

app = FastAPI(
    title="Enterprise LLM Security Gateway",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "LLM Security Gateway Running"
    }


@app.get("/dashboard")
def dashboard():
    return get_audit_statistics()


@app.post("/chat")
def chat(request: ChatRequest):

    # Step 1: Authentication
    if not authenticate_user(request.username):

        save_log(
            request.username,
            request.prompt,
            "BLOCKED"
        )

        raise HTTPException(
            status_code=401,
            detail="Unauthorized User"
        )

    # Step 2: Rate Limiting
    if not check_rate_limit(request.username):

        save_log(
            request.username,
            request.prompt,
            "RATE_LIMITED"
        )

        raise HTTPException(
            status_code=429,
            detail="Rate Limit Exceeded"
        )

    # Step 3: DLP Sanitization
    redacted_prompt = sanitize_prompt(request.prompt)

    # Step 4: Prompt Injection Detection
    if detect_prompt_injection(request.prompt):

        save_log(
            request.username,
            redacted_prompt,
            "PROMPT_INJECTION_BLOCKED"
        )

        raise HTTPException(
            status_code=403,
            detail="Prompt Injection Attack Detected"
        )

    # Step 5: SQL Injection Detection
    if detect_sql_injection(request.prompt):

        save_log(
            request.username,
            redacted_prompt,
            "SQL_INJECTION_BLOCKED"
        )

        raise HTTPException(
            status_code=403,
            detail="SQL Injection Attempt Detected"
        )

    # Step 6: Audit Logging
    save_log(
        request.username,
        redacted_prompt,
        "ALLOWED"
    )

    # Step 7: Response
    return {
        "status": "success",
        "username": request.username,
        "original_prompt": request.prompt,
        "redacted_prompt": redacted_prompt,
        "message": "Request Processed Successfully"
    }