import uuid
from datetime import UTC, datetime

from pydantic import TypeAdapter

from tribute_api.v1.models.enums import TributeCurrency, TributeOrderStatus
from tribute_api.v1.models.enums.shop import TributeShopStatus
from tribute_api.v1.models.enums.webhooks import TributeNotificationType
from tribute_api.v1.models.shop import TributeShopInfo
from tribute_api.v1.models.webhooks.notification import TributeWebhookNotification


def test_tribute_shop_info_parsing():
    json_data = {
        "user_id": 123,
        "name": "My Shop",
        "link": "myshop",
        "callback_url": "https://example.com/webhook",
        "recurrent": True,
        "only_stars": False,
        "status": 1,
    }

    shop = TributeShopInfo.model_validate(json_data)

    assert shop.user_id == 123
    assert shop.name == "My Shop"
    assert shop.link == "myshop"
    assert str(shop.callback_url) == "https://example.com/webhook"
    assert shop.recurrent is True
    assert shop.only_stars is False
    assert shop.status == TributeShopStatus.ACTIVE


def test_webhook_shop_order_parsing():
    order_uuid = str(uuid.uuid4())
    now = datetime.now(UTC).isoformat()
    json_data = {
        "name": "shop_order",
        "created_at": now,
        "sent_at": now,
        "payload": {
            "uuid": order_uuid,
            "amount": 1000,
            "currency": "rub",
            "fee": 100,
            "status": "paid",
            "email": "test@example.com",
            "is_recurrent": False,
        },
    }

    adapter = TypeAdapter(TributeWebhookNotification)
    notification = adapter.validate_python(json_data)

    assert notification.name == TributeNotificationType.SHOP_ORDER
    assert str(notification.payload.uuid) == order_uuid
    assert notification.payload.amount == 1000
    assert notification.payload.currency == TributeCurrency.RUB
    assert notification.payload.status == TributeOrderStatus.PAID
    assert notification.payload.email == "test@example.com"
