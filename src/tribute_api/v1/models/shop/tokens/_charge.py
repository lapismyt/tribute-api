from datetime import datetime
from uuid import UUID

from pydantic import Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.enums import TributeCurrency
from tribute_api.v1.enums.shop.tokens import TributeChargeStatus


class TributeShopCharge(TributeModel):
    charge_uuid: UUID = Field(
        ...,
        description="Charge UUID",
        examples=[UUID("550e8400-e29b-41d4-a716-446655440000")],
    )
    status: TributeChargeStatus = Field(
        ...,
        description="Charge status",
        examples=[TributeChargeStatus.PROCESSING],
    )
    reference: str | None = Field(
        None,
        description="Merchant reference (optional)",
        examples=["order-123"],
        max_length=256,
    )
    amount: int = Field(
        ...,
        description="Charge amount in smallest currency units",
        examples=[100000],
    )
    currency: TributeCurrency = Field(
        ...,
        description="Currency code (lowercase)",
        examples=[TributeCurrency.USD],
    )
    token: UUID | None = Field(
        ...,
        description="Payment token UUID",
        examples=[UUID("550e8400-e29b-41d4-a716-446655440000")],
    )
    error_code: str | None = Field(
        None,
        description="Error code if charge failed (optional)",
        examples=["payment_declined"],
    )
    error_message: str | None = Field(
        None,
        description="Error message if charge failed (optional)",
        examples=["Card was declined by the issuer"],
    )
    created_at: datetime = Field(
        ...,
        description="Charge creation timestamp in ISO 8601 format",
        examples=[datetime.fromisoformat("2025-03-20T01:15:58Z")],
    )
    processed_at: datetime | None = Field(
        None,
        description="Charge processing completion timestamp (optional)",
        examples=[datetime.fromisoformat("2025-03-20T01:16:02Z")],
    )
