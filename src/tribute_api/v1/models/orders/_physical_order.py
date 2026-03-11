from datetime import datetime

from pydantic import EmailStr, Field

from tribute_api.base.models import TributeModel
from tribute_api.v1.models.orders._address import TributeAddress
from tribute_api.v1.models.orders._order_item import TributeOrderItem
from tribute_api.v1.models.orders._physical_order_status import (
    TributePhysicalOrderStatus,
)


class TributePhysicalOrder(TributeModel):
    id: int = Field(..., examples=[12345])
    """Unique order identifier."""

    status: TributePhysicalOrderStatus = Field(
        ..., examples=[TributePhysicalOrderStatus.PENDING]
    )
    """Order status."""

    created: datetime = Field(
        ..., examples=[datetime.fromisoformat("2024-01-15T10:30:00Z")]
    )
    """Order creation date and time."""

    full_name: str = Field(..., examples=["John Doe"])
    """Recipient full name."""

    email: EmailStr = Field(..., examples=["john@example.com"])
    """Recipient email."""

    phone: str = Field(..., examples=["+1234567890"])
    """Recipient phone."""

    telegram_id: int = Field(
        ...,
        examples=[123456789],
        validation_alias="telegramID",
        serialization_alias="telegramID",
    )
    """Buyer's Telegram ID."""

    address: TributeAddress = Field(..., examples=[TributeAddress()])
    """Recipient address."""

    locality: str = Field(..., examples=["New York"])
    """City."""

    full_address: str = Field(..., examples=["USA, New York, 5th Avenue, 123, Apt 45"])
    """Full delivery address."""

    customer_note: str = Field(..., examples=["Please call before delivery"])
    """Customer note."""

    items: list[TributeOrderItem] = Field(...)
    """Order items."""

    delivery_cost: int | float = Field(...)
    """Delivery cost."""

    currency: str = Field(..., examples=["usd"])
    """Order currency."""
