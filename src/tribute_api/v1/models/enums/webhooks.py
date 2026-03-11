from enum import StrEnum


class TributeNotificationType(StrEnum):
    SHOP_ORDER = "shop_order"
    SHOP_ORDER_CHARGE_FAILED = "shop_order_charge_failed"
    SHOP_ORDER_CHARGE_SUCCESS = "shop_order_charge_success"
    SHOP_ORDER_CANCELLED = "shop_order_cancelled"
    SHOP_TOKEN_CHARGE_SUCCESS = "shop_token_charge_success"  # noqa: S105
    SHOP_TOKEN_CHARGE_FAILED = "shop_token_charge_failed"  # noqa: S105
    SHOP_ORDER_REFUNDED = "shop_order_refunded"
    SHOP_ORDER_PAYMENT_FAILED = "shop_order_payment_failed"
    NEW_SUBSCRIPTION = "new_subscription"
    CANCELLED_SUBSCRIPTION = "cancelled_subscription"
    RENEWED_SUBSCRIPTION = "renewed_subscription"
    PHYSICAL_ORDER_CREATED = "physical_order_created"
    PHYSICAL_ORDER_SHIPPED = "physical_order_shipped"
    PHYSICAL_ORDER_CANCELED = "physical_order_canceled"
    NEW_DONATION = "new_donation"
    RECURRENT_DONATION = "recurrent_donation"
    CANCELLED_DONATION = "cancelled_donation"
    NEW_DIGITAL_PRODUCT_PURCHASE = "new_digital_product"
    DIGITAL_PRODUCT_REFUNDED = "digital_product_refunded"


class TributeShopOrderCancelReason(StrEnum):
    CANCELLED_BY_SELLER = "cancelled_by_seller"
    CHARGE_FAILED = "charge_failed"
    PAYMENT_METHOD_EXPIRED = "payment_method_expired"


class TributeSubscriptionPeriod(StrEnum):
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    YEARLY = "yearly"


class TributeSubscriptionType(StrEnum):
    REGULAR = "regular"
    GIFT = "gift"
    TRIAL = "trial"
