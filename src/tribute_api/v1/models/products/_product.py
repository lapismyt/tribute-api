from datetime import datetime

from pydantic import Field, HttpUrl

from tribute_api.base.models import TributeModel
from tribute_api.v1.models.enums import TributeCurrency
from tribute_api.v1.models.products._status import TributeProductStatus
from tribute_api.v1.models.products._type import TributeProductType


class TributeProduct(TributeModel):
    id: int = Field(..., examples=[2548])
    """Product ID."""

    type: TributeProductType = Field(..., examples=[TributeProductType.DIGITAL])
    """Product type."""

    name: str = Field(..., examples=["VPN Access - 1 Month"])
    """Product name."""

    description: str | None = Field(
        None,
        examples=[
            (
                "High-speed VPN service with unlimited bandwidth and"
                " 50+ server locations worldwide"
            )
        ],
    )
    """Product description."""

    amount: int = Field(
        ...,
        examples=[499],
    )
    """Product price in smallest currency units (cents for USD/EUR, kopecks for RUB)."""

    currency: TributeCurrency = Field(..., examples=[TributeCurrency.RUB])
    """Currency code."""

    stars_amount: int | None = Field(None, examples=[100])
    """Price in Telegram Stars."""

    stars_amount_enabled: bool | None = Field(None, examples=[True])
    """Whether payment with Stars is enabled."""

    status: TributeProductStatus = Field(..., examples=[TributeProductStatus.APPROVED])
    """Product status."""

    is_custom: bool = Field(..., examples=[False])
    """Whether this is a custom product."""

    accept_cards: bool = Field(..., examples=[True])
    """Whether card payments are accepted."""

    accept_wallet_pay: bool = Field(..., examples=[False])
    """Whether wallet payments are accepted."""

    protect_content: bool = Field(..., examples=[True])
    """Whether content protection is enabled."""

    created: datetime = Field(
        ..., examples=[datetime.fromisoformat("2025-08-25T10:30:00Z")]
    )
    """Product creation date."""

    updated: datetime = Field(
        ..., examples=[datetime.fromisoformat("2025-08-25T10:30:00Z")]
    )
    """Product last update date."""

    pending_orders: int | None = Field(None, examples=[3])
    """Number of pending orders (for custom products)."""

    image_url: HttpUrl | None = Field(
        None, examples=["https://cdn.example.com/image.jpg"]
    )
    """Product image URL."""

    link: HttpUrl = Field(..., examples=["https://t.me/tribute_bot/app?startapp=pf6"])
    """Direct link to product in Telegram app."""

    web_link: HttpUrl = Field(..., examples=["https://web.tribute.tg/p/f6"])
    """Web link to product."""
