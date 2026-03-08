from pydantic import Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.models.shop import TributeTransaction


class TributeGetShopOrderTransactionsResponse(TributeModel):
    transactions: list[TributeTransaction] = Field(
        ...,
        description="List of transactions",
        examples=[],
    )
    next_from: str = Field(
        ...,
        description="Offset for the next page. Empty string if no more pages",
        examples=["20"],
    )
