from pydantic import Field

from tribute_api.base.models import TributeModel


class TributeCancelRecurringShopOrderResponse(TributeModel):
    success: bool = Field(
        ...,
        description="Whether the operation was successful",
        examples=[True],
    )
    message: str = Field(
        ...,
        description="Success message",
        examples=["recurring order cancelled"],
    )
