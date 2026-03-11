from pydantic import BaseModel, Field


class TributeWebhookSuccessResponse(BaseModel):
    status: str | None = Field(None, examples=["ok"])
