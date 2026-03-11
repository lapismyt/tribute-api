from pydantic import Field

from tribute_api.base.models import TributeModel


class TributeCancelRecurringShopOrderResponse(TributeModel):
    success: bool = Field(..., examples=[True])
    """Whether the operation was successful."""

    message: str = Field(..., examples=["recurring order cancelled"])
    """Success message."""
