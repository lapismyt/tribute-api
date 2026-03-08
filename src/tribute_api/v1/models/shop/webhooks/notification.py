from typing import Annotated

from pydantic import Discriminator

from tribute_api.v1.models.shop.webhooks.shop_order import TributeShopOrderNotification
from tribute_api.v1.models.shop.webhooks.shop_order_charge_failed import (
    TributeShopOrderChargeFailedNotification,
)
from tribute_api.v1.models.shop.webhooks.shop_order_charge_success import (
    TributeShopOrderChargeSuccessNotification,
)
from tribute_api.v1.models.shop.webhooks.shop_order_payment_failed import (
    TributeShopOrderPaymentFailedNotification,
)
from tribute_api.v1.models.shop.webhooks.shop_order_refunded import (
    TributeShopOrderRefundedNotification,
)

TributeWebhookNotification = Annotated[
    TributeShopOrderNotification
    | TributeShopOrderChargeFailedNotification
    | TributeShopOrderChargeSuccessNotification
    | TributeShopOrderPaymentFailedNotification
    | TributeShopOrderRefundedNotification,
    Discriminator("name"),
]
