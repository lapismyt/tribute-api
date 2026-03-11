from typing import Literal
from uuid import UUID

from pydantic import Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.models.enums import TributeCurrency
from tribute_api.v1.models.enums.webhooks import TributeNotificationType
from tribute_api.v1.models.webhooks._base import TributeBaseNotification


class TributeShopTokenChargeFailedPayload(TributeModel):
    """Notification when a merchant-initiated token charge fails."""

    charge_uuid: UUID = Field(
        ..., examples=[UUID("550e8400-e29b-41d4-a716-446655440000")]
    )
    """Charge UUID."""

    token: UUID = Field(..., examples=[UUID("660e8400-e29b-41d4-a716-446655440001")])
    """Payment token UUID."""

    amount: int = Field(..., examples=[100000])
    """Charge amount in smallest currency units."""

    currency: TributeCurrency = Field(..., examples=[TributeCurrency.RUB])
    """Currency code (lowercase)."""

    reference: str | None = Field(None, examples=["order-123"])
    """Merchant reference (optional)."""

    error_code: str = Field(..., examples=["payment_declined"])
    """Error code."""

    error_message: str = Field(..., examples=["Card was declined by the issuer"])
    """Detailed error message."""


class TributeShopTokenChargeFailedNotification(TributeBaseNotification):
    """Notification when a merchant-initiated token charge fails."""

    name: Literal[TributeNotificationType.SHOP_TOKEN_CHARGE_FAILED]
    payload: TributeShopTokenChargeFailedPayload
