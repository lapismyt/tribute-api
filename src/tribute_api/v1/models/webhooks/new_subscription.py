from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

from tribute_api.v1.models.enums.webhooks import (
    TributeNotificationType,
    TributeSubscriptionPeriod,
    TributeSubscriptionType,
)
from tribute_api.v1.models.webhooks._base import TributeBaseNotification


class TributeNewSubscriptionPayload(BaseModel):
    """Notification about user purchasing a subscription."""

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

    type: TributeSubscriptionType | None = Field(
        None, examples=[TributeSubscriptionType.REGULAR]
    )
    """Subscription type."""

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

    channel_id: int = Field(..., examples=[614])
    """Channel ID."""

    channel_name: str = Field(..., examples=["lbs"])
    """Channel name."""

    expires_at: datetime = Field(
        ..., examples=[datetime.fromisoformat("2025-04-20T01:15:57.305733Z")]
    )
    """Subscription expiration date."""


class TributeNewSubscriptionNotification(TributeBaseNotification):
    """Notification about user purchasing a subscription."""

    name: Literal[TributeNotificationType.NEW_SUBSCRIPTION]
    payload: TributeNewSubscriptionPayload
