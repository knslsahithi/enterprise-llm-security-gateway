from pydantic import BaseModel

class ChatRequest(BaseModel):
    username: str
    model: str
    prompt: str