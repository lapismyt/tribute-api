from typing import Literal
from uuid import UUID

from pydantic import EmailStr, Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.models.enums import (
    TributeBillingPeriod,
    TributeCurrency,
    TributeOrderStatus,
)
from tribute_api.v1.models.enums.webhooks import TributeNotificationType
from tribute_api.v1.models.webhooks._base import TributeBaseNotification


class TributeShopOrderPayload(TributeModel):
    """Notification about a shop order payment completion."""

    uuid: UUID = Field(..., examples=[UUID("550e8400-e29b-41d4-a716-446655440000")])
    """Order UUID."""

    amount: int = Field(..., examples=[100000])
    """Order amount in smallest currency units (cents/kopecks)."""

    currency: TributeCurrency = Field(..., examples=[TributeCurrency.RUB])
    """Currency code (lowercase)."""

    fee: int = Field(..., examples=[8000])
    """Platform fee in smallest currency units."""

    status: Literal[TributeOrderStatus.PAID] = Field(
        ..., examples=[TributeOrderStatus.PAID]
    )
    """Order status (webhook is sent only when status = 'paid')."""

    email: EmailStr | None = Field(None, examples=["customer@example.com"])
    """Customer email (optional, may be empty)."""

    is_recurrent: bool = Field(..., examples=[False])
    """Whether this is a recurring order."""

    period: TributeBillingPeriod | None = Field(
        None, examples=[TributeBillingPeriod.MONTHLY]
    )
    """Billing period (only for recurring orders)."""


class TributeShopOrderNotification(TributeBaseNotification):
    """Notification about a shop order payment completion."""

    name: Literal[TributeNotificationType.SHOP_ORDER]
    payload: TributeShopOrderPayload
