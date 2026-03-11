from typing import Literal

from pydantic import BaseModel, Field, HttpUrl

from tribute_api.v1.models.enums.webhooks import (
    TributeNotificationType,
    TributeSubscriptionPeriod,
)
from tribute_api.v1.models.webhooks._base import TributeBaseNotification


class TributeRecurrentDonationPayload(BaseModel):
    """Notification about a recurring donation payment."""

    donation_request_id: int = Field(..., examples=[123])
    """Donation request ID."""

    donation_name: str = Field(..., examples=["Monthly support"])
    """Donation name."""

    period: TributeSubscriptionPeriod = Field(
        ..., examples=[TributeSubscriptionPeriod.MONTHLY]
    )
    """Donation period."""

    amount: int = Field(..., examples=[500])
    """Donation amount in smallest currency units."""

    currency: str = Field(..., examples=["eur"])
    """Currency."""

    anonymously: bool = Field(..., examples=[False])
    """Whether the donation is anonymous."""

    web_app_link: HttpUrl = Field(
        ..., examples=["https://t.me/tribute/app?startapp=d456"]
    )
    """Link to view donation in web app."""

    user_id: int | None = Field(None, examples=[31326])
    """Deprecated legacy user ID in the system (if not anonymous)."""

    trb_user_id: str | None = Field(
        None,
        examples=["W-15408"],
    )
    """Tribute user ID with prefix (if not anonymous).
    `T-<user_id>` for users authorized via telegram,
    `W-<user_id>` for users authorized via email.
    """

    telegram_user_id: int | None = Field(None, examples=[12321321])
    """User's Telegram ID (if not anonymous)."""

    telegram_username: str | None = Field(None, examples=["durov"])
    """User's Telegram username, without @ (if not anonymous)."""


class TributeRecurrentDonationNotification(TributeBaseNotification):
    """Notification about a recurring donation payment."""

    name: Literal[TributeNotificationType.RECURRENT_DONATION]
    payload: TributeRecurrentDonationPayload
