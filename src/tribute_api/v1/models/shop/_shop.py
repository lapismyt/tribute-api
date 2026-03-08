from pydantic import Field, HttpUrl

from tribute_api.base.models import TributeModel
from tribute_api.v1.enums.shop import TributeShopStatus


class TributeShopInfo(TributeModel):
    user_id: int = Field(
        ...,
        description="Shop owner user ID",
        examples=[123],
    )
    name: str = Field(
        ...,
        description="Shop name",
        examples=["My Shop"],
    )
    link: str = Field(
        ...,
        description="Shop link/slug",
        examples=["myshop"],
    )
    callback_url: HttpUrl = Field(
        ...,
        description="Webhook callback URL for order notifications",
        examples=["https://example.com/webhook"],
    )
    recurrent: bool = Field(
        ...,
        description="Whether recurring payments are available",
        examples=[True],
    )
    only_stars: bool = Field(
        ...,
        description="Whether only Telegram Stars payment is accepted",
        examples=[False],
    )
    status: TributeShopStatus = Field(
        ...,
        description="Shop status (0 = inactive, 1 = active)",
        examples=[TributeShopStatus.ACTIVE],
    )
