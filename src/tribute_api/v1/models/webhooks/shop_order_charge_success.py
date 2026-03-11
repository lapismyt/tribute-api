from typing import Literal
from uuid import UUID

from pydantic import EmailStr, Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.models.enums import TributeBillingPeriod, TributeCurrency
from tribute_api.v1.models.enums.webhooks import TributeNotificationType
from tribute_api.v1.models.webhooks._base import TributeBaseNotification


class TributeShopOrderChargeSuccessPayload(TributeModel):
    """Notification when a recurring shop order is charged successfully."""

    uuid: UUID = Field(..., examples=[UUID("550e8400-e29b-41d4-a716-446655440000")])
    """Order UUID."""

    amount: int = Field(..., examples=[100000])
    """Order amount in smallest currency units (cents/kopecks)."""

    currency: TributeCurrency = Field(..., examples=[TributeCurrency.RUB])
    """Currency code (lowercase)."""

    period: TributeBillingPeriod = Field(..., examples=[TributeBillingPeriod.MONTHLY])
    """Billing period."""

    email: EmailStr | None = Field(None, examples=["customer@example.com"])
    """Customer email."""


class TributeShopOrderChargeSuccessNotification(TributeBaseNotification):
    """Notification when a recurring shop order is charged successfully."""

    name: Literal[TributeNotificationType.SHOP_ORDER_CHARGE_SUCCESS]
    payload: TributeShopOrderChargeSuccessPayload
