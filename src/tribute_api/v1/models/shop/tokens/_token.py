from datetime import datetime
from uuid import UUID

from pydantic import Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.enums import TributeCurrency


class TributeShopToken(TributeModel):
    token: UUID = Field(
        ...,
        description="Payment token UUID",
        examples=[UUID("550e8400-e29b-41d4-a716-446655440000")],
    )
    card_last4: str = Field(
        ...,
        description="Last 4 digits of the card number",
        examples=["1234"],
    )
    card_brand: str = Field(
        ...,
        description="Card brand (VISA, MASTERCARD, etc.)",
        examples=["VISA"],
    )
    customer_id: str | None = Field(
        None,
        description="Merchant's customer reference (optional)",
        examples=["user_12345"],
    )
    amount: int = Field(
        ...,
        description="Fixed charge amount in smallest currency units",
        examples=[100000],
    )
    currency: TributeCurrency = Field(
        ...,
        description="Currency code (lowercase)",
        examples=[TributeCurrency.RUB],
    )
    active: bool = Field(
        ...,
        description="Whether the token is active and can be charged",
        examples=[True],
    )
    created_at: datetime = Field(
        ...,
        description="Token creation timestamp in ISO 8601 format",
        examples=[datetime.fromisoformat("2025-03-20T01:15:58Z")],
    )
    last_used_at: datetime | None = Field(
        None,
        description="Last time the token was charged (optional)",
        examples=[datetime.fromisoformat("2025-03-25T12:30:00Z")],
    )
