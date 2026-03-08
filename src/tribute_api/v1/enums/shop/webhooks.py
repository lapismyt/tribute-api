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
