from typing import Literal
from uuid import UUID

from pydantic import EmailStr, Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.enums import TributeBillingPeriod, TributeCurrency
from tribute_api.v1.enums.shop.webhooks import TributeNotificationType
from tribute_api.v1.models.shop.webhooks._base import TributeBaseNotification


class TributeShopOrderChargeSuccessPayload(TributeModel):
    uuid: UUID = Field(
        ...,
        description="Order UUID",
        examples=[UUID("550e8400-e29b-41d4-a716-446655440000")],
    )
    amount: int = Field(
        ...,
        description="Order amount in smallest currency units (cents/kopecks)",
        examples=[100000],
    )
    currency: TributeCurrency = Field(
        ...,
        description="Currency code (lowercase)",
        examples=[TributeCurrency.RUB],
    )
    period: TributeBillingPeriod = Field(
        ...,
        description="Billing period",
        examples=[TributeBillingPeriod.MONTHLY],
    )
    email: EmailStr | None = Field(
        None,
        description="Customer email",
        examples=["customer@example.com"],
    )


class TributeShopOrderChargeSuccessNotification(TributeBaseNotification):
    name: Literal[TributeNotificationType.SHOP_ORDER_CHARGE_SUCCESS]
    payload: TributeShopOrderChargeSuccessPayload
