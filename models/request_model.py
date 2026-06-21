from pydantic import BaseModel

class ChatRequest(BaseModel):
    username: str
    prompt: str