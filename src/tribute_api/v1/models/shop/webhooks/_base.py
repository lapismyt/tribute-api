from datetime import datetime

from pydantic import BaseModel, Field


class TributeBaseNotification(BaseModel):
    created_at: datetime = Field(
        ...,
        description="Event creation time",
        examples=[datetime.fromisoformat("2025-03-20T01:15:58.33246Z")],
    )
    sent_at: datetime = Field(
        ...,
        description="Event sent time",
        examples=[datetime.fromisoformat("2025-03-20T01:15:58.542279448Z")],
    )
