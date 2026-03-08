from typing import Literal

from pydantic import Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.enums.shop import TributeRefundStatus


class TributeShopRefundTransactionResponse(TributeModel):
    success: bool = Field(
        ...,
        description="Whether the refund was successful",
        examples=[True],
    )
    message: str = Field(
        ...,
        description="Success message",
        examples=["refund initiated"],
    )
    status: Literal[TributeRefundStatus.INITIATED] = Field(
        ...,
        description="Refund status",
        examples=[TributeRefundStatus.INITIATED],
    )
