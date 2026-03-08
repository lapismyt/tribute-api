import logging

import aiohttp
from pydantic import SecretStr

from tribute_api._types import AnyUUID
from tribute_api.v1 import DEFAULT_BASE_URL
from tribute_api.v1.client_raw import TributeApiV1ClientRaw
from tribute_api.v1.enums import TributeOrderStatus
from tribute_api.v1.exceptions import TributeApiV1Error
from tribute_api.v1.models._error import TributeError
from tribute_api.v1.models.shop import (
    TributeCancelRecurringShopOrderResponse,
    TributeCreateShopOrderRequestBody,
    TributeCreateShopOrderResponse,
    TributeGetShopOrderStatusResponse,
    TributeGetShopOrderTransactionsResponse,
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

    async def get_shop_raw(self) -> TributeShopInfo | TributeError:
        return await self._handle_response(await self._get("/shop"), TributeShopInfo)

    async def get_shop(self) -> TributeShopInfo:
        result = await self.get_shop_raw()

        if isinstance(result, TributeError):
            raise TributeApiV1Error(result.error, result.message)

        return result

    async def get_shop_orders_raw(self) -> list[TributeShopOrder] | TributeError:
        return await self._handle_list_response(
            await self._get("/shop/orders"), TributeShopOrder
        )

    async def get_shop_orders(self) -> list[TributeShopOrder]:
        result = await self.get_shop_orders_raw()

        if isinstance(result, TributeError):
            raise TributeApiV1Error(result.error, result.message)

        return result

    async def create_shop_order_raw(
        self, body: TributeCreateShopOrderRequestBody
    ) -> TributeCreateShopOrderResponse | TributeError:
        return await self._handle_response(
            await self._post("/shop/orders", json=body.model_dump()),
            TributeCreateShopOrderResponse,
        )

    async def create_shop_order(
        self, body: TributeCreateShopOrderRequestBody
    ) -> TributeCreateShopOrderResponse:
        result = await self.create_shop_order_raw(body)

        if isinstance(result, TributeError):
            raise TributeApiV1Error(result.error, result.message)

        return result

    async def get_shop_order_status_raw(
        self, order_uuid: AnyUUID
    ) -> TributeGetShopOrderStatusResponse | TributeError:
        return await self._handle_response(
            await self._get(f"/shop/orders/{self._uuid_to_str(order_uuid)}/status"),
            TributeGetShopOrderStatusResponse,
        )

    async def get_shop_order_status(self, order_uuid: AnyUUID) -> TributeOrderStatus:
        result = await self.get_shop_order_status_raw(order_uuid)

        if isinstance(result, TributeError):
            raise TributeApiV1Error(result.error, result.message)

        return result.status

    async def cancel_recurring_shop_order_raw(
        self, order_uuid: AnyUUID
    ) -> TributeCancelRecurringShopOrderResponse | TributeError:
        return await self._handle_response(
            await self._post(
                f"/shop/orders/{self._uuid_to_str(order_uuid)}/cancel",
            ),
            TributeCancelRecurringShopOrderResponse,
        )

    async def cancel_recurring_shop_order(
        self, order_uuid: AnyUUID
    ) -> TributeCancelRecurringShopOrderResponse:
        result = await self.cancel_recurring_shop_order_raw(order_uuid)

        if isinstance(result, TributeError):
            raise TributeApiV1Error(result.error, result.message)

        return result

    async def get_shop_order_transactions_raw(
        self, order_uuid: AnyUUID, start_from: str | None = None
    ) -> TributeGetShopOrderTransactionsResponse | TributeError:
        return await self._handle_response(
            await self._get(
                f"/shop/orders/{self._uuid_to_str(order_uuid)}/transactions",
                params={"startFrom": start_from},
            ),
            TributeGetShopOrderTransactionsResponse,
        )

    async def get_shop_order_transactions(
        self, order_uuid: AnyUUID, limit: int | None = 128
    ) -> list[TributeTransaction]:
        transactions_full: list[TributeTransaction] = []

        start_from = None

        while not limit or len(transactions_full) < limit:
            result = await self.get_shop_order_transactions_raw(
                order_uuid, start_from=start_from
            )

            if isinstance(result, TributeError):
                raise TributeApiV1Error(result.error, result.message)

            transactions_full.extend(result.transactions)
            start_from = result.next_from

        return transactions_full

    async def refund_shop_order_transaction_raw(
        self, order_uuid: AnyUUID, tx_id: int
    ) -> TributeShopRefundTransactionResponse | TributeError:
        return await self._handle_response(
            await self._post(
                f"/shop/orders/{self._uuid_to_str(order_uuid)}/transactions/{tx_id}/refund"
            ),
            TributeShopRefundTransactionResponse,
        )

    async def refund_shop_order_transaction(
        self, order_uuid: AnyUUID, tx_id: int
    ) -> TributeShopRefundTransactionResponse:
        result = await self.refund_shop_order_transaction_raw(order_uuid, tx_id)

        if isinstance(result, TributeError):
            raise TributeApiV1Error(result.error, result.message)

        return result

    async def list_shop_tokens(
        self,
        customer_id: str | None = None,
        order_uuid: AnyUUID | None = None,
        active: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> list[TributeShopToken]:
        result = await self.list_shop_tokens_raw(
            customer_id, order_uuid, active, limit, offset
        )

        if isinstance(result, TributeError):
            raise TributeApiV1Error(result.error, result.message)

        return result

    async def get_shop_token(self, token_uuid: AnyUUID) -> TributeShopToken:
        result = await self.get_shop_token_raw(token_uuid)

        if isinstance(result, TributeError):
            raise TributeApiV1Error(result.error, result.message)

        return result

    async def deactivate_shop_token(
        self, token_uuid: AnyUUID
    ) -> TributeDeactivateShopTokenResponse:
        result = await self.deactivate_shop_token_raw(token_uuid)

        if isinstance(result, TributeError):
            raise TributeApiV1Error(result.error, result.message)

        return result

    async def create_shop_charge(
        self, body: TributeCreateShopChargeRequestBody
    ) -> TributeShopCharge:
        result = await self.create_shop_charge_raw(body)

        if isinstance(result, TributeError):
            raise TributeApiV1Error(result.error, result.message)

        return result

    async def get_shop_charge(self, charge_uuid: AnyUUID) -> TributeShopCharge:
        result = await self.get_shop_charge_raw(charge_uuid)

        if isinstance(result, TributeError):
            raise TributeApiV1Error(result.error, result.message)

        return result
