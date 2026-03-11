from typing import Annotated

from pydantic import Discriminator

from tribute_api.v1.models.webhooks import (
    TributeShopOrderCancelledNotification,
    TributeShopTokenChargeFailedNotification,
    TributeShopTokenChargeSuccessNotification,
)
from tribute_api.v1.models.webhooks.cancelled_donation import (
    TributeCancelledDonationNotification,
)
from tribute_api.v1.models.webhooks.cancelled_subscription import (
    TributeCancelledSubscriptionNotification,
)
from tribute_api.v1.models.webhooks.digital_product_refunded import (
    TributeDigitalProductRefundedNotification,
)
from tribute_api.v1.models.webhooks.new_digital_product_purchase import (
    TributeNewDigitalProductPurchaseNotification,
)
from tribute_api.v1.models.webhooks.new_donation import TributeNewDonationNotification
from tribute_api.v1.models.webhooks.new_subscription import (
    TributeNewSubscriptionNotification,
)
from tribute_api.v1.models.webhooks.physical_order_canceled import (
    TributePhysicalOrderCanceledNotification,
)
from tribute_api.v1.models.webhooks.physical_order_created import (
    TributePhysicalOrderCreatedNotification,
)
from tribute_api.v1.models.webhooks.physical_order_shipped import (
    TributePhysicalOrderShippedNotification,
)
from tribute_api.v1.models.webhooks.recurrent_donation import (
    TributeRecurrentDonationNotification,
)
from tribute_api.v1.models.webhooks.renewed_subscription import (
    TributeRenewedSubscriptionNotification,
)
from tribute_api.v1.models.webhooks.shop_order import TributeShopOrderNotification
from tribute_api.v1.models.webhooks.shop_order_charge_failed import (
    TributeShopOrderChargeFailedNotification,
)
from tribute_api.v1.models.webhooks.shop_order_charge_success import (
    TributeShopOrderChargeSuccessNotification,
)
from tribute_api.v1.models.webhooks.shop_order_payment_failed import (
    TributeShopOrderPaymentFailedNotification,
)
from tribute_api.v1.models.webhooks.shop_order_refunded import (
    TributeShopOrderRefundedNotification,
)

TributeWebhookNotification = Annotated[
    TributeShopOrderNotification
    | TributeShopOrderChargeFailedNotification
    | TributeShopOrderChargeSuccessNotification
    | TributeShopOrderPaymentFailedNotification
    | TributeShopOrderRefundedNotification
    | TributeShopTokenChargeFailedNotification
    | TributeShopTokenChargeSuccessNotification
    | TributeShopOrderCancelledNotification
    | TributeNewSubscriptionNotification
    | TributeCancelledSubscriptionNotification
    | TributeRenewedSubscriptionNotification
    | TributePhysicalOrderCreatedNotification
    | TributePhysicalOrderShippedNotification
    | TributePhysicalOrderCanceledNotification
    | TributeNewDonationNotification
    | TributeRecurrentDonationNotification
    | TributeCancelledDonationNotification
    | TributeNewDigitalProductPurchaseNotification
    | TributeDigitalProductRefundedNotification,
    Discriminator("name"),
]
