from pydantic import Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.enums import TributeCurrency


class TributeTransaction(TributeModel):
    id: int = Field(..., description="Transaction ID", examples=[12345])
    type: str = Field(..., description="Transaction type", examples=["shop_order_sell"])
    object_id: int | None = Field(None, description="Related object ID", examples=[100])
    amount: int | float = Field(
        ...,
        description="Transaction amount in currency units (e.g., EUR, RUB)",
        examples=[1000],
    )
    currency: TributeCurrency = Field(
        ..., description="Currency code (lowercase)", examples=[TributeCurrency.RUB]
    )
    created_at: int = Field(
        ...,
        description="Transaction creation timestamp (Unix timestamp in seconds)",
        examples=[1731510245],
    )
    service_fee: int | float | None = Field(
        None,
        description="Service fee amount",
        examples=[80],
    )
    total: int | float = Field(
        ...,
        description="Total amount after fees",
        examples=[920],
    )
    payment_method: str | None = Field(
        None,
        description="Payment method used",
        examples=["bank_card"],
    )
    is_refunded: bool | None = Field(
        None,
        description="Whether the transaction has been refunded",
        examples=[False],
    )
    is_refundable: bool | None = Field(
        None,
        description="Whether the transaction can be refunded",
        examples=[True],
    )
    is_recurring: bool | None = Field(
        None,
        description="Whether this is a recurring payment transaction",
        examples=[False],
    )
