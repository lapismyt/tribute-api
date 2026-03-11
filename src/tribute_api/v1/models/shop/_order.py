from datetime import datetime
from uuid import UUID

from pydantic import EmailStr, Field, HttpUrl, field_validator

from tribute_api.base.models import TributeModel
from tribute_api.v1.models.enums import TributeCurrency
from tribute_api.v1.models.enums.shop import (
    TributeBillingPeriod,
    TributeMemberStatus,
    TributeOrderStatus,
)


class TributeShopOrder(TributeModel):
    uuid: UUID = Field(..., examples=[UUID("550e8400-e29b-41d4-a716-446655440000")])
    """Order UUID."""

    amount: int = Field(..., examples=[100000])
    """Order amount in smallest currency units (cents/kopecks)."""

    currency: TributeCurrency = Field(..., examples=[TributeCurrency.RUB])
    """Currency code (lowercase)."""

    title: str = Field(..., examples=["Product X"])
    """Order title (max 100 UTF-16 characters)."""

    description: str = Field(..., examples=["Detailed product description"])
    """Order description (max 500 UTF-16 characters)."""

    status: TributeOrderStatus = Field(..., examples=[TributeOrderStatus.PAID])
    """Order status."""

    email: EmailStr | None = Field(None, examples=["customer@example.com"])
    """Customer email (optional)."""

    success_url: HttpUrl = Field(..., examples=[HttpUrl("https://shop.com/success")])
    """Redirect URL on successful payment."""

    failure_url: HttpUrl = Field(..., examples=[HttpUrl("https://shop.com/fail")])
    """Redirect URL on failed payment."""

    payment_url: HttpUrl = Field(
        ...,
        examples=[
            HttpUrl(
                "https://web.tribute.tg/shop/pay/550e8400-e29b-41d4-a716-446655440000"
            )
        ],
    )
    """URL for customer to complete payment."""

    created_at: datetime = Field(
        ..., examples=[datetime.fromisoformat("2025-11-13T15:04:05Z")]
    )
    """Order creation timestamp in ISO 8601 format."""

    comment: str | None = Field(None, examples=["Special request"])
    """Optional comment for the order."""

    period: TributeBillingPeriod = Field(..., examples=[TributeBillingPeriod.ONETIME])
    """Billing period for recurring orders."""

    member_status: TributeMemberStatus | None = Field(
        None, examples=[TributeMemberStatus.ACTIVE]
    )
    """Recurring subscription status (only for recurring orders)."""

    member_expires_at: datetime | None = Field(
        None,
        description=(
            "Recurring subscription expiration date in ISO 8601 format"
            " (only for recurring orders)"
        ),
        examples=[datetime.fromisoformat("2025-12-13T15:04:05Z")],
    )
    """Recurring subscription expiration date in ISO 8601 format
    (only for recurring orders).
    """

    @field_validator("title")
    @classmethod
    def check_title_utf16_len(cls, v: str) -> str:
        utf16_len = len(v.encode("utf-16-le")) // 2
        if utf16_len > 100:
            msg = "Title must be max 100 UTF-16 characters"
            raise ValueError(msg)
        return v

    @field_validator("description")
    @classmethod
    def check_description_utf16_len(cls, v: str) -> str:
        utf16_len = len(v.encode("utf-16-le")) // 2
        if utf16_len > 300:
            msg = "Description must be max 300 UTF-16 characters"
            raise ValueError(msg)
        return v
