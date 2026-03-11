from pydantic import Field

from tribute_api.base.models import TributeModel


class TributeCancelDigitalProductPurchaseResponse(TributeModel):
    success: bool = Field(..., examples=[True])
    """Operation success status."""

    purchase_id: int = Field(..., examples=[12345])
    """Cancelled purchase ID."""

    message: str = Field(..., examples=["purchase cancelled and payment refunded"])
    """Success message."""
