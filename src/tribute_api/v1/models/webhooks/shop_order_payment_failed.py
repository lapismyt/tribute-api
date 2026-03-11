from typing import Literal
from uuid import UUID

from pydantic import EmailStr, Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.models.enums import (
    TributeCurrency,
)
from tribute_api.v1.models.enums.webhooks import TributeNotificationType
from tribute_api.v1.models.webhooks._base import TributeBaseNotification


class TributeShopOrderPaymentFailedPayload(TributeModel):
    """Notification when an initial shop order payment fails
        (e.g., card declined, insufficient funds).
    This is sent for one-time payments that fail during the initial payment attempt.
    """

    uuid: UUID = Field(..., examples=[UUID("550e8400-e29b-41d4-a716-446655440000")])
    """Order UUID."""

    amount: int = Field(..., examples=[100000])
    """Order amount in smallest currency units (cents/kopecks)."""

    currency: TributeCurrency = Field(..., examples=[TributeCurrency.RUB])
    """Currency code (lowercase)."""

    error_code: str = Field(..., examples=["payment_declined"])
    """Error code indicating the type of failure."""

    error_message: str = Field(..., examples=["Card declined by issuer"])
    """Human-readable error message describing the failure reason."""

    email: EmailStr | None = Field(None, examples=["customer@example.com"])
    """Customer email (optional)."""


class TributeShopOrderPaymentFailedNotification(TributeBaseNotification):
    """Notification when an initial shop order payment fails
        (e.g., card declined, insufficient funds).
    This is sent for one-time payments that fail during the initial payment attempt.
    """

    name: Literal[TributeNotificationType.SHOP_ORDER_PAYMENT_FAILED]
    payload: TributeShopOrderPaymentFailedPayload
