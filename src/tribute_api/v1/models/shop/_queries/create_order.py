from uuid import UUID

from pydantic import EmailStr, Field, HttpUrl, field_validator

from tribute_api.base.models import TributeModel
from tribute_api.v1.models.enums import TributeCurrency
from tribute_api.v1.models.enums.shop import TributeBillingPeriod


class TributeCreateShopOrderRequestBody(TributeModel):
    amount: int = Field(
        ...,
        examples=[100000],
    )
    """Order amount in smallest currency units (cents for EUR/USD, kopecks for RUB)."""

    currency: TributeCurrency = Field(..., examples=[TributeCurrency.RUB])
    """Currency code (lowercase)."""

    title: str = Field(..., examples=["Product X"], max_length=100)
    """Order title (required, max 100 UTF-16 characters)."""

    description: str = Field(
        ..., examples=["Detailed product description"], max_length=300
    )
    """Order description (required, max 300 UTF-16 characters)."""

    success_url: HttpUrl | None = Field(
        None, examples=[HttpUrl("https://shop.com/success")]
    )
    """Redirect URL on successful payment (optional, must be valid URL)."""

    fail_url: HttpUrl | None = Field(None, examples=[HttpUrl("https://shop.com/fail")])
    """Redirect URL on failed payment (optional, must be valid URL)."""

    email: EmailStr | None = Field(None, examples=["customer@example.com"])
    """Customer email (optional, validated if provided)."""

    save_payment_method: bool | None = Field(
        None,
        examples=[False],
    )
    """Whether to save payment method for recurring charges
    (requires shop.recurrent to be enabled).
    """

    comment: str | None = Field(None, examples=["Special request"])
    """Optional comment for the order."""

    customer_id: str | None = Field(None, max_length=256, examples=["user_12345"])
    """Unique customer identifier."""

    period: TributeBillingPeriod | None = Field(
        None,
        examples=[TributeBillingPeriod.MONTHLY],
    )

    """Billing period. Defaults to "onetime" if not specified.
    Recurring periods require shop.recurrent to be enabled.
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


class TributeCreateShopOrderResponse(TributeModel):
    uuid: UUID = Field(..., examples=[UUID("550e8400-e29b-41d4-a716-446655440000")])
    """Order UUID."""
    payment_url: HttpUrl = Field(
        ...,
        examples=[
            "https://web.tribute.tg/shop/pay/550e8400-e29b-41d4-a716-446655440000"
        ],
    )
    """Payment URL for customer to complete payment."""
