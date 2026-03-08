from typing import Literal
from uuid import UUID

from pydantic import EmailStr, Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.enums import (
    TributeCurrency,
)
from tribute_api.v1.enums.shop.webhooks import TributeNotificationType
from tribute_api.v1.models.shop.webhooks._base import TributeBaseNotification


class TributeShopOrderPaymentFailedPayload(TributeModel):
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
    error_code: str = Field(
        ...,
        description="Error code indicating the type of failure",
        examples=["payment_declined"],
    )
    error_message: str = Field(
        ...,
        description="Human-readable error message describing the failure reason",
        examples=["Card declined by issuer"],
    )
    email: EmailStr | None = Field(
        None,
        description="Customer email (optional)",
        examples=["customer@example.com"],
    )


class TributeShopOrderPaymentFailedNotification(TributeBaseNotification):
    name: Literal[TributeNotificationType.SHOP_ORDER_PAYMENT_FAILED]
    payload: TributeShopOrderPaymentFailedPayload
