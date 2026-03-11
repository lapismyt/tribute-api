from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

from tribute_api.v1.models.enums.webhooks import (
    TributeNotificationType,
)
from tribute_api.v1.models.webhooks._base import TributeBaseNotification


class TributeNewDigitalProductPurchasePayload(BaseModel):
    """Notification about a digital product purchase."""

    product_id: int = Field(..., examples=[456])
    """Digital product ID."""

    product_name: str = Field(..., examples=["VPN Access - 1 Month"])
    """Digital product name."""

    amount: int = Field(..., examples=[500])
    """Amount paid in smallest currency units."""

    currency: str = Field(..., examples=["usd"])
    """Currency."""

    user_id: int | None = Field(None, examples=[31326], deprecated=True)
    """Deprecated legacy user ID in the system."""

    trb_user_id: int | None = Field(
        None,
        examples=["T-31326"],
    )
    """Tribute user ID with prefix.
    `T-<user_id>` for users authorized via telegram,
    `W-<user_id>` for users authorized via email.
    """

    telegram_user_id: int | None = Field(None, examples=[12321321])
    """User's Telegram ID."""

    telegram_username: int | None = Field(None, examples=["durov"])
    """User's Telegram username (without @)."""

    purchase_id: int = Field(
        ...,
        examples=[78901],
    )
    """Unique purchase ID.
    Use this to identify individual purchases and for idempotency.
    """

    transaction_id: int = Field(..., examples=[234567])
    """Transaction ID for tracking the payment."""

    purchase_created_at: datetime = Field(
        ..., examples=[datetime.fromisoformat("2025-03-20T01:15:58.33246Z")]
    )
    """Purchase creation timestamp."""


class TributeNewDigitalProductPurchaseNotification(TributeBaseNotification):
    """Notification about a digital product purchase."""

    name: Literal[TributeNotificationType.NEW_DIGITAL_PRODUCT_PURCHASE]
    payload: TributeNewDigitalProductPurchasePayload
