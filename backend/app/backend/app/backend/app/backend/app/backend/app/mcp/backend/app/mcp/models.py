from pydantic import BaseModel


class MCPRequest(BaseModel):
    tool: str
    input: dict


class MCPResponse(BaseModel):
    success: bool
    output: dict
