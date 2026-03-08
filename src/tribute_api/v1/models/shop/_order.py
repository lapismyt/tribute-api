from datetime import datetime
from uuid import UUID

from pydantic import EmailStr, Field, HttpUrl, field_validator

from tribute_api.base.models import TributeModel
from tribute_api.v1.enums import TributeCurrency
from tribute_api.v1.enums.shop import (
    TributeBillingPeriod,
    TributeMemberStatus,
    TributeOrderStatus,
)


class TributeShopOrder(TributeModel):
    uuid: UUID = Field(
        ...,
        description="Order UUID",
        examples=[UUID("550e8400-e29b-41d4-a716-446655440000")],
    )
    amount: int = Field(
        ...,
        description="Order amount in smallest currency units (cents/kopecks)",
        examples=[100000],
    )
    currency: TributeCurrency = Field(
        ...,
        description="Currency code (lowercase)",
        examples=[TributeCurrency.RUB],
    )
    title: str = Field(
        ...,
        description="Order title (max 100 UTF-16 characters)",
        examples=["Product X"],
    )
    description: str = Field(
        ...,
        description="Order description (max 500 UTF-16 characters)",
        examples=["Detailed product description"],
    )
    status: TributeOrderStatus = Field(
        ...,
        description="Order status",
        examples=[TributeOrderStatus.PAID],
    )
    email: EmailStr | None = Field(
        None,
        description="Customer email (optional)",
        examples=["customer@example.com"],
    )
    success_url: HttpUrl = Field(
        ...,
        description="Redirect URL on successful payment",
        examples=[HttpUrl("https://shop.com/success")],
    )
    failure_url: HttpUrl = Field(
        ...,
        description="Redirect URL on failed payment",
        examples=[HttpUrl("https://shop.com/fail")],
    )
    payment_url: HttpUrl = Field(
        ...,
        description="URL for customer to complete payment",
        examples=[
            HttpUrl(
                "https://web.tribute.tg/shop/pay/550e8400-e29b-41d4-a716-446655440000"
            )
        ],
    )
    created_at: datetime = Field(
        ...,
        description="Order creation timestamp in ISO 8601 format",
        examples=[datetime.fromisoformat("2025-11-13T15:04:05Z")],
    )
    comment: str | None = Field(
        None,
        description="Optional comment for the order",
        examples=["Special request"],
    )
    period: TributeBillingPeriod = Field(
        ...,
        description="Billing period for recurring orders",
        examples=[TributeBillingPeriod.ONETIME],
    )
    member_status: TributeMemberStatus | None = Field(
        None,
        description="Recurring subscription status (only for recurring orders)",
        examples=[TributeMemberStatus.ACTIVE],
    )
    member_expires_at: datetime | None = Field(
        None,
        description=(
            "Recurring subscription expiration date in ISO 8601 format"
            " (only for recurring orders)"
        ),
        examples=[datetime.fromisoformat("2025-12-13T15:04:05Z")],
    )

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
