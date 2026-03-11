from typing import Literal

from pydantic import BaseModel, EmailStr, Field, HttpUrl

from tribute_api.v1.models.enums.webhooks import (
    TributeNotificationType,
)
from tribute_api.v1.models.webhooks._base import TributeBaseNotification


class TributeNewDonationPayload(BaseModel):
    """Notification about a new donation."""

    donation_request_id: int = Field(..., examples=[123])
    """Donation request ID."""

    donation_name: str = Field(..., examples=["Support my work"])
    """Donation name."""

    message: str | None = Field(None, examples=["Thank you for your content!"])
    """Donation message."""

    period: str = Field(..., examples=["once"])
    """Donation period (once for one-time donation)."""

    amount: int = Field(..., examples=[1000])
    """Donation amount in smallest currency units."""

    currency: str = Field(..., examples=["usd"])
    """Currency."""

    anonymously: bool = Field(..., examples=[False])
    """Whether the donation is anonymous."""

    web_app_link: HttpUrl = Field(
        ..., examples=["https://t.me/tribute/app?startapp=d123"]
    )
    """Link to view donation in web app."""

    email: EmailStr | None = Field(None, examples=["donor@example.com"])
    """Donor email (for web donations)."""

    user_id: int | None = Field(None, examples=[31326])
    """Deprecated legacy user ID in the system (if not anonymous)."""

    trb_user_id: str | None = Field(None, examples=["T-31326"])
    """Tribute user ID with prefix (if not anonymous).
    `T-<user_id>` for users authorized via telegram,
    `W-<user_id>` for users authorized via email.
    """

    telegram_user_id: int | None = Field(None, examples=[12321321])
    """User's Telegram ID (if not anonymous)."""

    telegram_username: str | None = Field(None, examples=["durov"])
    """User's Telegram username, without @ (if not anonymous)."""


class TributeNewDonationNotification(TributeBaseNotification):
    """Notification about a new donation."""

    name: Literal[TributeNotificationType.NEW_DONATION]
    payload: TributeNewDonationPayload
