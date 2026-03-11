from datetime import datetime
from typing import Literal

from pydantic import BaseModel, EmailStr, Field, HttpUrl

from tribute_api.v1.models.enums.webhooks import (
    TributeNotificationType,
    TributeSubscriptionPeriod,
    TributeSubscriptionType,
)
from tribute_api.v1.models.webhooks._base import TributeBaseNotification


class TributeRenewedSubscriptionPayload(BaseModel):
    """Notification about subscription renewal."""

    subscription_name: str = Field(..., examples=["Support creativity 🌟"])
    """Subscription name."""

    subscription_id: int = Field(..., examples=[1644])
    """Subscription ID."""

    period_id: int = Field(..., examples=[1547])
    """Subscription period ID."""

    period: TributeSubscriptionPeriod = Field(
        ..., examples=[TributeSubscriptionPeriod.MONTHLY]
    )
    """Subscription period."""

    price: int = Field(..., examples=[1000])
    """Subscription price in smallest currency units."""

    amount: int = Field(..., examples=[700])
    """Amount after commission deduction in smallest currency units."""

    currency: str = Field(..., examples=["eur"])
    """Currency code."""

    user_id: int = Field(..., examples=[31326], deprecated=True)
    """Deprecated legacy user ID in the system."""

    trb_user_id: str = Field(..., examples=["T-31326"])
    """Tribute user ID with prefix.
    `T-<user_id>` for users authorized via telegram,
    `W-<user_id>` for users authorized via email.
    """

    telegram_user_id: int = Field(..., examples=[12321321])
    """User's Telegram ID."""

    telegram_username: str | None = Field(None, examples=["durov"])
    """User's Telegram username (without @)."""

    email: EmailStr | None = Field(None, examples=["user@example.com"])
    """User email (optional, may be empty)."""

    web_app_link: HttpUrl | None = Field(
        None, examples=["https://t.me/metal3devbot/app?startapp=syX"]
    )
    """Link to subscription in web app."""

    channel_id: int = Field(..., examples=[614])
    """Channel ID."""

    channel_name: str = Field(..., examples=["lbs"])
    """Channel name."""

    expires_at: datetime = Field(
        ..., examples=[datetime.fromisoformat("2025-04-20T01:15:57.305733Z")]
    )
    """Subscription expiration date."""

    type: TributeSubscriptionType = Field(
        ..., examples=[TributeSubscriptionType.REGULAR]
    )
    """Subscription type."""


class TributeRenewedSubscriptionNotification(TributeBaseNotification):
    """Notification about subscription renewal."""

    name: Literal[TributeNotificationType.RENEWED_SUBSCRIPTION]
    payload: TributeRenewedSubscriptionPayload
