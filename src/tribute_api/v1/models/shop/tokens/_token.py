from datetime import datetime
from uuid import UUID

from pydantic import Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.models.enums import TributeCurrency


class TributeShopToken(TributeModel):
    token: UUID = Field(..., examples=[UUID("550e8400-e29b-41d4-a716-446655440000")])
    """Payment token UUID."""

    card_last4: str = Field(..., examples=["1234"])
    """Last 4 digits of the card number."""

    card_brand: str = Field(..., examples=["VISA"])
    """Card brand (VISA, MASTERCARD, etc.)."""

    customer_id: str | None = Field(None, examples=["user_12345"])
    """Merchant's customer reference (optional)."""

    amount: int = Field(..., examples=[100000])
    """Fixed charge amount in smallest currency units."""

    currency: TributeCurrency = Field(..., examples=[TributeCurrency.RUB])
    """Currency code (lowercase)."""

    active: bool = Field(..., examples=[True])
    """Whether the token is active and can be charged."""

    created_at: datetime = Field(
        ..., examples=[datetime.fromisoformat("2025-03-20T01:15:58Z")]
    )
    """Token creation timestamp in ISO 8601 format."""

    last_used_at: datetime | None = Field(
        None, examples=[datetime.fromisoformat("2025-03-25T12:30:00Z")]
    )
    """Last time the token was charged (optional)."""
