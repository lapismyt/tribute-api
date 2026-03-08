from datetime import datetime
from typing import Literal
from uuid import UUID

from pydantic import Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.enums import (
    TributeCurrency,
    TributeRefundStatus,
)
from tribute_api.v1.enums.shop.webhooks import TributeNotificationType
from tribute_api.v1.models.shop.webhooks._base import TributeBaseNotification


class TributeShopOrderRefundedPayload(TributeModel):
    uuid: UUID = Field(
        ...,
        description="Order UUID",
        examples=[UUID("550e8400-e29b-41d4-a716-446655440000")],
    )
    transaction_id: int = Field(
        ...,
        description="ID of the refunded transaction",
        examples=[12345],
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
    status: TributeRefundStatus = Field(
        ...,
        description="Refund status",
        examples=[TributeRefundStatus.INITIATED],
    )
    refunded_at: datetime | None = Field(
        None,
        description=(
            "Time when the refund was completed"
            " (optional, only present when status is 'completed')"
        ),
        examples=[datetime.fromisoformat("2025-03-20T01:15:58.33246Z")],
    )


class TributeShopOrderRefundedNotification(TributeBaseNotification):
    name: Literal[TributeNotificationType.SHOP_ORDER_REFUNDED]
    payload: TributeShopOrderRefundedPayload
