from typing import Literal

from pydantic import Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.models.enums.shop import TributeRefundStatus


class TributeShopRefundTransactionResponse(TributeModel):
    success: bool = Field(..., examples=[True])
    """Whether the refund was successful."""

    message: str = Field(..., examples=["refund initiated"])
    """Success message."""

    status: Literal[TributeRefundStatus.INITIATED] = Field(
        ..., examples=[TributeRefundStatus.INITIATED]
    )
    """Refund status."""
