from typing import Literal
from uuid import UUID

from pydantic import EmailStr, Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.enums import (
    TributeBillingPeriod,
    TributeCurrency,
    TributeOrderStatus,
)
from tribute_api.v1.enums.shop.webhooks import TributeNotificationType
from tribute_api.v1.models.shop.webhooks._base import (
    TributeBaseNotification,
)


class TributeShopOrderPayload(TributeModel):
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
    fee: int = Field(
        ...,
        description="Platform fee in smallest currency units",
        examples=[8000],
    )
    status: Literal[TributeOrderStatus.PAID] = Field(
        ...,
        description="Order status (webhook is sent only when status = 'paid')",
        examples=[TributeOrderStatus.PAID],
    )
    email: EmailStr | None = Field(
        None,
        description="Customer email (optional, may be empty)",
        examples=["customer@example.com"],
    )
    is_recurrent: bool = Field(
        ...,
        description="Whether this is a recurring order",
        examples=[False],
    )
    period: TributeBillingPeriod | None = Field(
        None,
        description="Billing period (only for recurring orders)",
        examples=[TributeBillingPeriod.MONTHLY],
    )


class TributeShopOrderNotification(TributeBaseNotification):
    name: Literal[TributeNotificationType.SHOP_ORDER]
    payload: TributeShopOrderPayload
