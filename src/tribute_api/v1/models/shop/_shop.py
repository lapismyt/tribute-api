from pydantic import Field, HttpUrl

from tribute_api.base.models import TributeModel
from tribute_api.v1.models.enums.shop import TributeShopStatus


class TributeShopInfo(TributeModel):
    user_id: int = Field(..., examples=[123])
    """Shop owner user ID."""

    name: str = Field(..., examples=["My Shop"])
    """Shop name."""

    link: str = Field(..., examples=["myshop"])
    """Shop link/slug."""

    callback_url: HttpUrl = Field(..., examples=["https://example.com/webhook"])
    """Webhook callback URL for order notifications."""

    recurrent: bool = Field(..., examples=[True])
    """Whether recurring payments are available."""

    only_stars: bool = Field(..., examples=[False])
    """Whether only Telegram Stars payment is accepted."""

    status: TributeShopStatus = Field(..., examples=[TributeShopStatus.ACTIVE])
    """Shop status (0 = inactive, 1 = active)."""
