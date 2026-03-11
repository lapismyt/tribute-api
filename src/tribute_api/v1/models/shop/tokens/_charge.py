from datetime import datetime
from uuid import UUID

from pydantic import Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.models.enums import TributeCurrency
from tribute_api.v1.models.enums.shop.tokens import TributeChargeStatus


class TributeShopCharge(TributeModel):
    charge_uuid: UUID = Field(
        ..., examples=[UUID("550e8400-e29b-41d4-a716-446655440000")]
    )
    """Charge UUID."""

    status: TributeChargeStatus = Field(..., examples=[TributeChargeStatus.PROCESSING])
    """Charge status."""

    reference: str | None = Field(None, examples=["order-123"], max_length=256)
    """Merchant reference (optional)."""

    amount: int = Field(..., examples=[100000])
    """Charge amount in smallest currency units."""

    currency: TributeCurrency = Field(..., examples=[TributeCurrency.USD])
    """Currency code (lowercase)."""

    token: UUID | None = Field(
        ..., examples=[UUID("550e8400-e29b-41d4-a716-446655440000")]
    )
    """Payment token UUID."""

    error_code: str | None = Field(None, examples=["payment_declined"])
    """Error code if charge failed (optional)."""

    error_message: str | None = Field(
        None, examples=["Card was declined by the issuer"]
    )
    """Error message if charge failed (optional)."""

    created_at: datetime = Field(
        ..., examples=[datetime.fromisoformat("2025-03-20T01:15:58Z")]
    )
    """Charge creation timestamp in ISO 8601 format."""

    processed_at: datetime | None = Field(
        None, examples=[datetime.fromisoformat("2025-03-20T01:16:02Z")]
    )
    """Charge processing completion timestamp (optional)."""
