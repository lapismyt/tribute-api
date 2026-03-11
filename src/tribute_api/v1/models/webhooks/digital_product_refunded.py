from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

from tribute_api.v1.models.enums.webhooks import (
    TributeNotificationType,
)
from tribute_api.v1.models.webhooks._base import TributeBaseNotification


class TributeDigitalProductRefundedPayload(BaseModel):
    """Notification about a digital product purchase."""

    product_id: int = Field(..., examples=[456])
    """Digital product ID."""

    product_name: str = Field(..., examples=["VPN Access - 1 Month"])
    """Digital product name."""

    amount: int = Field(..., examples=[500])
    """Refunded amount in smallest currency units."""

    currency: str = Field(..., examples=["usd"])
    """Currency."""

    user_id: int | None = Field(None, examples=[31326], deprecated=True)
    """Deprecated legacy buyer user ID in the system."""

    trb_user_id: int | None = Field(
        None,
        examples=["T-31326"],
    )
    """Tribute user ID with prefix.
    `T-<user_id>` for users authorized via telegram,
    `W-<user_id>` for users authorized via email.
    """

    telegram_user_id: int | None = Field(None, examples=[12321321])
    """Buyer's Telegram ID."""

    telegram_username: int | None = Field(None, examples=["durov"])
    """Buyer's Telegram username (without @)."""

    purchase_id: int = Field(
        ...,
        examples=[78901],
    )
    """Original purchase ID.
    Use this to match with the original new_digital_product webhook.
    """

    transaction_id: int = Field(..., examples=[234567])
    """Transaction ID that was refunded"""

    refund_reason: str = Field(
        ...,
        examples=["telegram_refund"],
    )
    """Reason for the refund:
    - `telegram_refund` - User refunded Stars through App Store or Google Play;
    - `Cancel product purchase from public API` - Creator initiated refund via API.
    """

    refunded_at: datetime = Field(
        ..., examples=[datetime.fromisoformat("2025-03-20T02:30:00.33246Z")]
    )
    """Timestamp when the refund was processed."""


class TributeDigitalProductRefundedNotification(TributeBaseNotification):
    """Notification about a digital product refund.

    This webhook is triggered when:
    - A user refunds Stars through App Store, Google Play, or their bank;
    - A creator initiates a refund via the API;

    **Important:** Use purchase_id to match refunds with original purchases and
        revoke access to digital content.
    """

    name: Literal[TributeNotificationType.DIGITAL_PRODUCT_REFUNDED]
    payload: TributeDigitalProductRefundedPayload
