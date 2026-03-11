from datetime import datetime

from pydantic import BaseModel, Field


class TributeBaseNotification(BaseModel):
    created_at: datetime = Field(
        ...,

        examples=[datetime.fromisoformat("2025-03-20T01:15:58.33246Z")])
    """Event creation time"""
    sent_at: datetime = Field(
        ...,

        examples=[datetime.fromisoformat("2025-03-20T01:15:58.542279448Z")])
    """Event sent time"""
