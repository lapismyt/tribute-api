from datetime import datetime
from typing import Literal
from uuid import UUID

from pydantic import Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.models.enums import (
    TributeCurrency,
    TributeRefundStatus,
)
from tribute_api.v1.models.enums.webhooks import TributeNotificationType
from tribute_api.v1.models.webhooks._base import TributeBaseNotification


class TributeShopOrderRefundedPayload(TributeModel):
    """Notification when a shop order transaction is refunded."""

    uuid: UUID = Field(..., examples=[UUID("550e8400-e29b-41d4-a716-446655440000")])
    """Order UUID."""

    transaction_id: int = Field(..., examples=[12345])
    """ID of the refunded transaction."""

    amount: int = Field(..., examples=[100000])
    """Order amount in smallest currency units (cents/kopecks)."""

    currency: TributeCurrency = Field(..., examples=[TributeCurrency.RUB])
    """Currency code (lowercase)."""

    status: TributeRefundStatus = Field(..., examples=[TributeRefundStatus.INITIATED])
    """Refund status."""

    refunded_at: datetime | None = Field(
        None,
        examples=[datetime.fromisoformat("2025-03-20T01:15:58.33246Z")],
    )
    """Time when the refund was completed
    (optional, only present when status is 'completed')."""


class TributeShopOrderRefundedNotification(TributeBaseNotification):
    """Notification when a shop order transaction is refunded."""

    name: Literal[TributeNotificationType.SHOP_ORDER_REFUNDED]
    payload: TributeShopOrderRefundedPayload
