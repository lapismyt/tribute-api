from uuid import UUID

from pydantic import EmailStr, Field, HttpUrl, field_validator

from tribute_api.base.models import TributeModel
from tribute_api.v1.enums import TributeCurrency
from tribute_api.v1.enums.shop import TributeBillingPeriod


class TributeCreateShopOrderRequestBody(TributeModel):
    amount: int = Field(
        ...,
        description=(
            "Order amount in smallest currency units"
            " (cents for EUR/USD, kopecks for RUB)"
        ),
        examples=[100000],
    )
    currency: TributeCurrency = Field(
        ...,
        description="Currency code (lowercase)",
        examples=[TributeCurrency.RUB],
    )
    title: str = Field(
        ...,
        description="Order title (required, max 100 UTF-16 characters)",
        examples=["Product X"],
        max_length=100,
    )
    description: str = Field(
        ...,
        description="Order description (required, max 300 UTF-16 characters)",
        examples=["Detailed product description"],
        max_length=300,
    )
    success_url: HttpUrl | None = Field(
        None,
        description="Redirect URL on successful payment (optional, must be valid URL)",
        examples=[HttpUrl("https://shop.com/success")],
    )
    fail_url: HttpUrl | None = Field(
        None,
        description="Redirect URL on failed payment (optional, must be valid URL)",
        examples=[HttpUrl("https://shop.com/fail")],
    )
    email: EmailStr | None = Field(
        None,
        description="Customer email (optional, validated if provided)",
        examples=["customer@example.com"],
    )
    save_payment_method: bool | None = Field(
        None,
        description=(
            "Whether to save payment method for recurring charges"
            " (requires shop.recurrent to be enabled)"
        ),
        examples=[False],
    )
    comment: str | None = Field(
        None,
        description="Optional comment for the order",
        examples=["Special request"],
    )
    customer_id: str | None = Field(
        None,
        description="Unique customer identifier",
        max_length=256,
        examples=["user_12345"],
    )
    period: TributeBillingPeriod | None = Field(
        None,
        description=(
            'Billing period. Defaults to "onetime" if not specified.'
            " Recurring periods require shop.recurrent to be enabled"
        ),
        examples=[TributeBillingPeriod.MONTHLY],
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


class TributeCreateShopOrderResponse(TributeModel):
    uuid: UUID = Field(
        ...,
        description="Order UUID",
        examples=[UUID("550e8400-e29b-41d4-a716-446655440000")],
    )
    payment_url: HttpUrl = Field(
        ...,
        description="Payment URL for customer to complete payment",
        examples=[
            "https://web.tribute.tg/shop/pay/550e8400-e29b-41d4-a716-446655440000"
        ],
    )
