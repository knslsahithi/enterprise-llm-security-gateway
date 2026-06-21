from fastapi import FastAPI, HTTPException

from models.request_model import ChatRequest
from services.auth_service import authenticate_user
from services.rate_limit_service import check_rate_limit
from services.db_log_service import save_log

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

    save_log(
        request.username,
        request.prompt,
        "ALLOWED"
    )

    return {
        "status": "success",
        "message": "Prompt Accepted",
        "prompt": request.prompt
    }