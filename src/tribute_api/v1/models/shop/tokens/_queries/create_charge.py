from uuid import UUID

from pydantic import Field

from tribute_api.base.models import TributeModel


class TributeCreateShopChargeRequestBody(TributeModel):
    token: UUID = Field(
        ...,
        description="The payment token UUID to charge",
        examples=[UUID("550e8400-e29b-41d4-a716-446655440000")],
    )
    amount: int = Field(
        ...,
        description="Charge amount in smallest currency units (cents/kopecks)",
        examples=[100000],
    )
    reference: str | None = Field(
        None,
        description="Merchant reference for this charge (optional, max 256 chars)",
        examples=["order-123"],
        max_length=256,
    )
    idempotency_key: str | None = Field(
        None,
        description="Unique key to prevent duplicate charges (optional, max 64 chars)",
        examples=["charge-req-abc123"],
        max_length=64,
    )
