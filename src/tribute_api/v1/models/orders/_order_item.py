from pydantic import Field

from tribute_api.base.models import TributeModel


class TributeOrderItem(TributeModel):
    id: int = Field(..., examples=[567])
    """Product variant ID."""

    price: int | float = Field(..., examples=[150])
    """Unit price."""

    quantity: int = Field(..., examples=[2])
    """Quantity."""

    currency: str = Field(..., examples=["usd"])
    """Currency."""

    name: str = Field(..., examples=["T-shirt with print"])
    """Product name."""

    attributes: dict = Field(..., examples=[{"size": "L", "color": "Black"}])
    """Product attributes."""
