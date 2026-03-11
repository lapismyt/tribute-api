from pydantic import Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.models.enums import TributeCurrency


class TributeTransaction(TributeModel):
    id: int = Field(..., examples=[12345])
    """Transaction ID."""

    type: str = Field(..., examples=["shop_order_sell"])
    """Transaction type."""

    object_id: int | None = Field(None, examples=[100])
    """Related object ID."""

    amount: int | float = Field(..., examples=[1000])
    """Transaction amount in currency units (e.g., EUR, RUB)."""

    currency: TributeCurrency = Field(..., examples=[TributeCurrency.RUB])
    """Currency code (lowercase)."""

    created_at: int = Field(..., examples=[1731510245])
    """Transaction creation timestamp (Unix timestamp in seconds)."""

    service_fee: int | float | None = Field(None, examples=[80])
    """Service fee amount."""

    total: int | float = Field(..., examples=[920])
    """Total amount after fees."""

    payment_method: str | None = Field(None, examples=["bank_card"])
    """Payment method used."""

    is_refunded: bool | None = Field(None, examples=[False])
    """Whether the transaction has been refunded."""

    is_refundable: bool | None = Field(None, examples=[True])
    """Whether the transaction can be refunded."""

    is_recurring: bool | None = Field(None, examples=[False])
    """Whether this is a recurring payment transaction."""
