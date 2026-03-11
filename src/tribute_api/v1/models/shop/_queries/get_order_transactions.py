from pydantic import Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.models.shop._transaction import TributeTransaction


class TributeGetShopOrderTransactionsResponse(TributeModel):
    transactions: list[TributeTransaction] = Field(..., examples=[])
    """List of transactions."""

    next_from: str = Field(..., examples=["20"])
    """Offset for the next page. Empty string if no more pages."""
