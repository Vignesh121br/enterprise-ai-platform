from pydantic import BaseModel


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatCompletionRequest(BaseModel):
    message: str
    session_id: str | None = None


class ChatCompletionResponse(BaseModel):
    response: str
    model: str
    session_id: str
