from uuid import UUID

from pydantic import Field

from tribute_api.base.models import TributeModel


class TributeCreateShopChargeRequestBody(TributeModel):
    token: UUID = Field(..., examples=[UUID("550e8400-e29b-41d4-a716-446655440000")])
    """The payment token UUID to charge."""

    amount: int = Field(..., examples=[100000])
    """Charge amount in smallest currency units (cents/kopecks)."""

    reference: str | None = Field(None, examples=["order-123"], max_length=256)
    """Merchant reference for this charge (optional, max 256 chars)."""

    idempotency_key: str | None = Field(
        None, examples=["charge-req-abc123"], max_length=64
    )
    """Unique key to prevent duplicate charges (optional, max 64 chars)."""
