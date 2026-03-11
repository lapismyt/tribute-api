from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

from tribute_api.v1.models.enums import TributeOrderStatus
from tribute_api.v1.models.enums.webhooks import (
    TributeNotificationType,
)
from tribute_api.v1.models.products import TributeProduct
from tribute_api.v1.models.webhooks._base import TributeBaseNotification


class TributePhysicalOrderShippedPayload(BaseModel):
    """Notification about physical order shipping."""

    order_id: int = Field(..., examples=[12345])
    """Order ID."""

    status: TributeOrderStatus = Field(..., examples=[TributeOrderStatus.PENDING])
    """Order status."""

    user_id: int = Field(..., examples=[31326], deprecated=True)
    """Deprecated legacy user ID in the system."""

    trb_user_id: int = Field(..., examples=["T-31326"])
    """Tribute user ID with prefix.
    `T-<user_id>` for users authorized via telegram,
    `W-<user_id>` for users authorized via email.
    """

    telegram_user_id: int = Field(..., examples=[12321321])
    """User's Telegram ID."""

    telegram_username: str = Field(..., examples=["durov"])
    """User's Telegram username (without @)."""

    products: list[TributeProduct] = Field(..., examples=[])
    """Order products."""

    total: int = Field(..., examples=[300000])
    """Total order amount in smallest currency units."""

    currency: str = Field(..., examples=["usd"])
    """Order currency."""

    shipping_address: str | None = Field(
        ..., examples=["USA, New York, 5th Avenue, 123, Apt 45"]
    )
    """Shipping address (only for shipped status)."""

    tracking_number: str | None = Field(..., examples=["US123456789CN"])
    """Tracking number (only for shipped status)."""

    created_at: datetime = Field(..., examples=["2025-03-20T01:15:58.33246Z"])
    """Order creation date."""

    updated_at: datetime = Field(..., examples=["2025-03-20T01:15:58.33246Z"])
    """Order update date."""


class TributePhysicalOrderShippedNotification(TributeBaseNotification):
    """Notification about physical order shipping."""

    name: Literal[TributeNotificationType.PHYSICAL_ORDER_SHIPPED]
    payload: TributePhysicalOrderShippedPayload
