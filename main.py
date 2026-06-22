from fastapi import FastAPI, HTTPException

from models.request_model import ChatRequest
from services.auth_service import authenticate_user
from services.rate_limit_service import check_rate_limit
from services.db_log_service import save_log
from services.dlp_service import sanitize_prompt

app = FastAPI(
    title="Enterprise LLM Security Gateway",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "LLM Security Gateway Running"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    # Step 1: Redact Sensitive Information
    redacted_prompt = sanitize_prompt(request.prompt)

    # Step 2: Authentication Check
    if not authenticate_user(request.username):

        save_log(
            request.username,
            redacted_prompt,
            "BLOCKED"
        )

        raise HTTPException(
            status_code=401,
            detail="Unauthorized User"
        )

    # Step 3: Rate Limiting Check
    if not check_rate_limit(request.username):

        save_log(
            request.username,
            redacted_prompt,
            "RATE_LIMITED"
        )

        raise HTTPException(
            status_code=429,
            detail="Rate Limit Exceeded"
        )

    # Step 4: Save Audit Log
    save_log(
        request.username,
        redacted_prompt,
        "ALLOWED"
    )

    # Step 5: Return Response
    return {
        "status": "success",
        "username": request.username,
        "original_prompt": request.prompt,
        "redacted_prompt": redacted_prompt
    }