import logging

import aiohttp
from pydantic import SecretStr

from tribute_api._types import AnyUUID
from tribute_api._utils import raise_from_error_tuple
from tribute_api.v1.client_raw import TributeApiV1ClientRaw
from tribute_api.v1.const import (
    DEFAULT_BASE_URL,
)
from tribute_api.v1.enums import TributeOrderStatus
from tribute_api.v1.models.shop import (
    TributeCancelRecurringShopOrderResponse,
    TributeCreateShopOrderRequestBody,
    TributeCreateShopOrderResponse,
    TributeShopInfo,
    TributeShopOrder,
    TributeShopRefundTransactionResponse,
    TributeTransaction,
)
from tribute_api.v1.models.shop.tokens import (
    TributeCreateShopChargeRequestBody,
    TributeDeactivateShopTokenResponse,
    TributeShopCharge,
    TributeShopToken,
)


class TributeApiV1Client(TributeApiV1ClientRaw):
    api_key: SecretStr
    base_url: str = DEFAULT_BASE_URL
    session: aiohttp.ClientSession | None = None

    def __init__(
        self,
        api_key: str | SecretStr,
        base_url: str = DEFAULT_BASE_URL,
        session: aiohttp.ClientSession | None = None,
        logger: logging.Logger | None = None,
        allow_insecure: bool = False,
    ):
        if isinstance(api_key, str):
            api_key = SecretStr(api_key)

        self.api_key = api_key
        self.base_url = base_url
        self.session = session
        self.logger = logger or logging.getLogger(__name__)
        self.allow_insecure = allow_insecure

    async def get_shop(self) -> TributeShopInfo:
        """Returns a list of saved payment tokens for the authenticated shop.
        Requires tokenCharging to be enabled for the shop.

        Returns:
            TributeShopInfo: Successful response.

        Raises:
            TributeApiV1Unauthorized: Unauthorized (invalid API key).
            TributeApiV1NotFound: Shop not found.
        """

        result = await self.get_shop_raw()

        if isinstance(result, tuple):
            return raise_from_error_tuple(result)

        return result

    async def get_shop_orders(self) -> list[TributeShopOrder]:
        """Returns a list of shop orders sorted by ID descending (newest first).

        Returns:
            list[TributeShopOrder]: Successful response.

        Raises:
            TributeApiV1Unauthorized: Unauthorized (invalid API key).
            TributeApiV1NotFound: Shop not found.
        """

        result = await self.get_shop_orders_raw()

        if isinstance(result, tuple):
            return raise_from_error_tuple(result)

        return result

    async def create_shop_order(
        self, body: TributeCreateShopOrderRequestBody
    ) -> TributeCreateShopOrderResponse:
        """Creates a new shop order and returns a payment URL for the customer.
        Supports one-time and recurring payments.

        Returns:
            TributeCreateShopOrderResponse: Order created successfully.

        Raises:
            TributeApiV1BadRequest: Bad request.
            TributeApiV1Unauthorized: Unauthorized (invalid API key).
            TributeApiV1NotFound: Shop not found.
        """

        result = await self.create_shop_order_raw(body)

        if isinstance(result, tuple):
            return raise_from_error_tuple(result)

        return result

    async def get_shop_order_status(self, order_uuid: AnyUUID) -> TributeOrderStatus:
        """Returns the current status of a specific shop order by its UUID.
        Only accessible by the shop owner.

        Returns:
            TributeOrderStatus: Successful response.

        Raises:
            TributeApiV1Forbidden: Forbidden (order belongs to another shop).
            TributeApiV1Unauthorized: Unauthorized (invalid API key).
            TributeApiV1NotFound: Order or shop not found.
        """

        result = await self.get_shop_order_status_raw(order_uuid)

        if isinstance(result, tuple):
            return raise_from_error_tuple(result)

        return result.status

    async def cancel_recurring_shop_order(
        self, order_uuid: AnyUUID
    ) -> TributeCancelRecurringShopOrderResponse:
        """Cancels a recurring shop order subscription.
        Only accessible by the shop owner or authorized managers.

        Returns:
            TributeCancelRecurringShopOrderResponse: Order canceled successfully.

        Raises:
            TributeApiV1BadRequest: Bad request.
            TributeApiV1Unauthorized: Unauthorized (invalid API key).
            TributeApiV1Forbidden: Forbidden (access denied).
            TributeApiV1NotFound: Order, shop, or recurring subscription not found.
        """

        result = await self.cancel_recurring_shop_order_raw(order_uuid)

        if isinstance(result, tuple):
            return raise_from_error_tuple(result)

        return result

    async def get_shop_order_transactions(
        self, order_uuid: AnyUUID, limit: int | None = 128
    ) -> list[TributeTransaction]:
        """Returns a paginated list of transactions for a specific shop order.
        Only accessible by the shop owner or authorized managers.

        Returns:
            list[TributeTransaction]: Successful response.

        Raises:
            TributeApiV1Unauthorized: Unauthorized (invalid API key).
            TributeApiV1Forbidden: Forbidden (access denied).
            TributeApiV1NotFound: Order or shop not found.
        """

        transactions_full: list[TributeTransaction] = []

        start_from = None

        while not limit or len(transactions_full) < limit:
            result = await self.get_shop_order_transactions_raw(
                order_uuid, start_from=start_from
            )

            if isinstance(result, tuple):
                return raise_from_error_tuple(result)

            transactions_full.extend(result.transactions)
            start_from = result.next_from

        return transactions_full

    async def refund_shop_order_transaction(
        self, order_uuid: AnyUUID, tx_id: int
    ) -> TributeShopRefundTransactionResponse:
        """Initiates a refund for a specific transaction of a shop order.
        Only accessible by the shop owner or authorized managers.
        Only sell transactions from paid orders can be refunded.

        Returns:
            TributeShopRefundTransactionResponse: Refund initiated successfully.

        Raises:
            TributeApiV1BadRequest: Bad request.
            TributeApiV1Unauthorized: Unauthorized (invalid API key).
            TributeApiV1Forbidden: Forbidden (access denied).
            TributeApiV1NotFound: Order, shop, or transaction not found.
            TributeApiV1ServerError: Internal server error (refund processing failed).
        """

        result = await self.refund_shop_order_transaction_raw(order_uuid, tx_id)

        if isinstance(result, tuple):
            return raise_from_error_tuple(result)

        return result

    async def list_shop_tokens(
        self,
        customer_id: str | None = None,
        order_uuid: AnyUUID | None = None,
        active: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> list[TributeShopToken]:
        """Returns a list of saved payment tokens for the authenticated shop.
        Requires tokenCharging to be enabled for the shop.

        Returns:
            list[TributeShopToken]: Successful response.

        Raises:
            TributeApiV1Unauthorized: Unauthorized (invalid API key).
            TributeApiV1Forbidden: Token charging not enabled for this shop.
            TributeApiV1NotFound: Shop not found.
        """

        result = await self.list_shop_tokens_raw(
            customer_id, order_uuid, active, limit, offset
        )

        if isinstance(result, tuple):
            return raise_from_error_tuple(result)

        return result

    async def get_shop_token(self, token_uuid: AnyUUID) -> TributeShopToken:
        """Returns details of a specific saved payment token.
        Requires tokenCharging to be enabled for the shop.

        Returns:
            TributeShopToken: Successful response.

        Raises:
            TributeApiV1Unauthorized: Unauthorized (invalid API key).
            TributeApiV1Forbidden: Token charging not enabled for this shop.
            TributeApiV1NotFound: Token or shop not found.
        """

        result = await self.get_shop_token_raw(token_uuid)

        if isinstance(result, tuple):
            return raise_from_error_tuple(result)

        return result

    async def deactivate_shop_token(
        self, token_uuid: AnyUUID
    ) -> TributeDeactivateShopTokenResponse:
        """Deactivates a saved payment token,
            preventing it from being used for future charges.
        Requires tokenCharging to be enabled for the shop.

        Returns:
            TributeDeactivateShopTokenResponse: Token deactivated successfully.

        Raises:
            TributeApiV1BadRequest: Bad request.
            TributeApiV1Unauthorized: Unauthorized (invalid API key).
            TributeApiV1Forbidden: Token charging not enabled for this shop.
            TributeApiV1NotFound: Token or shop not found.
        """

        result = await self.deactivate_shop_token_raw(token_uuid)

        if isinstance(result, tuple):
            return raise_from_error_tuple(result)

        return result

    async def create_shop_charge(
        self, body: TributeCreateShopChargeRequestBody
    ) -> TributeShopCharge:
        """Creates a new merchant-initiated charge against a saved payment token.
        The merchant specifies the charge amount in smallest currency units
            (cents/kopecks).
        Requires tokenCharging to be enabled for the shop.

        **Amount Limits** (in smallest currency units):
            - EUR: 100 - 300,000 (€1 - €3,000)
            - RUB: 10,000 - 30,000,000 (₽100 - ₽300,000)
            - USD: 100 - 300,000 ($1 - $3,000)

        **Rate limiting**:
            - 1 minute cooldown between charges on the same token
                (returns 429 with remaining seconds)
            - Only one pending charge per token at a time (returns 409)

        **Idempotency**: Use the idempotencyKey parameter to safely retry requests.
            If a charge with the same idempotency key already exists,
                the existing charge will be returned.


        Returns:
            TributeShopCharge: Charge created successfully.

        Raises:
            TributeApiV1BadRequest: Bad request.
            TributeApiV1Unauthorized: Unauthorized (invalid API key).
            TributeApiV1Forbidden: Token charging not enabled for this shop.
            TributeApiV1NotFound: Token or shop not found.
            TributeApiV1Conflict: Conflict - charge already pending.
            TributeApiV1TooManyRequests: Rate limit exceeded:
                must wait before charging again.
            TributeApiV1BadGateway: Payment gateway error.
        """

        result = await self.create_shop_charge_raw(body)

        if isinstance(result, tuple):
            return raise_from_error_tuple(result)

        return result

    async def get_shop_charge(self, charge_uuid: AnyUUID) -> TributeShopCharge:
        """Returns the status and details of a specific charge.
        Requires tokenCharging to be enabled for the shop.

        Returns:
            TributeShopCharge: Successful response.

        Raises:
            TributeApiV1Unauthorized: Unauthorized (invalid API key).
            TributeApiV1Forbidden: Token charging not enabled for this shop.
            TributeApiV1NotFound: Charge or shop not found.
        """

        result = await self.get_shop_charge_raw(charge_uuid)

        if isinstance(result, tuple):
            return raise_from_error_tuple(result)

        return result
