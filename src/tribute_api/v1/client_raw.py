import logging
from uuid import UUID

import aiohttp
from pydantic import SecretStr

from tribute_api._types import AnyUUID
from tribute_api.base.client import TributeApiBaseClient
from tribute_api.base.models import TributeModel
from tribute_api.v1 import DEFAULT_BASE_URL
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
)
from tribute_api.v1.models.shop.tokens import (
    TributeCreateShopChargeRequestBody,
    TributeDeactivateShopTokenResponse,
    TributeShopCharge,
    TributeShopToken,
)


class TributeApiV1ClientRaw(TributeApiBaseClient):
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

    @staticmethod
    async def _handle_response[T: TributeModel](
        resp: aiohttp.ClientResponse, response_class: type[T]
    ) -> T | TributeError:
        if resp.status == 200:
            return response_class.model_validate(await resp.json())
        return TributeError.model_validate(await resp.json())

    @staticmethod
    async def _handle_list_response[T: TributeModel](
        resp: aiohttp.ClientResponse, response_class: type[T]
    ) -> list[T] | TributeError:
        if resp.status == 200:
            return [response_class.model_validate(el) for el in await resp.json()]
        return TributeError.model_validate(await resp.json())

    @staticmethod
    def _uuid_to_str(uuid: AnyUUID) -> str:
        if isinstance(uuid, UUID):
            return str(uuid)
        return uuid

    async def get_shop_raw(self) -> TributeShopInfo | TributeError:
        return await self._handle_response(await self._get("/shop"), TributeShopInfo)

    async def get_shop_orders_raw(self) -> list[TributeShopOrder] | TributeError:
        return await self._handle_list_response(
            await self._get("/shop/orders"), TributeShopOrder
        )

    async def create_shop_order_raw(
        self, body: TributeCreateShopOrderRequestBody
    ) -> TributeCreateShopOrderResponse | TributeError:
        return await self._handle_response(
            await self._post("/shop/orders", json=body.model_dump()),
            TributeCreateShopOrderResponse,
        )

    async def get_shop_order_status_raw(
        self, order_uuid: AnyUUID
    ) -> TributeGetShopOrderStatusResponse | TributeError:
        return await self._handle_response(
            await self._get(f"/shop/orders/{self._uuid_to_str(order_uuid)}/status"),
            TributeGetShopOrderStatusResponse,
        )

    async def cancel_recurring_shop_order_raw(
        self, order_uuid: AnyUUID
    ) -> TributeCancelRecurringShopOrderResponse | TributeError:
        return await self._handle_response(
            await self._post(
                f"/shop/orders/{self._uuid_to_str(order_uuid)}/cancel",
            ),
            TributeCancelRecurringShopOrderResponse,
        )

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

    async def refund_shop_order_transaction_raw(
        self, order_uuid: AnyUUID, tx_id: int
    ) -> TributeShopRefundTransactionResponse | TributeError:
        return await self._handle_response(
            await self._post(
                f"/shop/orders/{self._uuid_to_str(order_uuid)}/transactions/{tx_id}/refund"
            ),
            TributeShopRefundTransactionResponse,
        )

    async def list_shop_tokens_raw(
        self,
        customer_id: str | None = None,
        order_uuid: AnyUUID | None = None,
        active: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> list[TributeShopToken] | TributeError:
        return await self._handle_list_response(
            await self._get(
                "/shop/tokens",
                params={
                    "customer_id": customer_id,
                    "order_uuid": self._uuid_to_str(order_uuid) if order_uuid else None,
                    "active": (
                        ("true" if active else "false") if active is not None else None
                    ),
                    "limit": limit,
                    "offset": offset,
                },
            ),
            TributeShopToken,
        )

    async def get_shop_token_raw(
        self, token_uuid: AnyUUID
    ) -> TributeShopToken | TributeError:
        return await self._handle_response(
            await self._get(
                f"/shop/tokens/{self._uuid_to_str(token_uuid)}",
            ),
            TributeShopToken,
        )

    async def deactivate_shop_token_raw(
        self, token_uuid: AnyUUID
    ) -> TributeDeactivateShopTokenResponse | TributeError:
        return await self._handle_response(
            await self._delete(f"/shop/tokens/{self._uuid_to_str(token_uuid)}"),
            TributeDeactivateShopTokenResponse,
        )

    async def create_shop_charge_raw(
        self, body: TributeCreateShopChargeRequestBody
    ) -> TributeShopCharge | TributeError:
        return await self._handle_response(
            await self._post("/shop/charges", json=body.model_dump()),
            TributeShopCharge,
        )

    async def get_shop_charge_raw(
        self, charge_uuid: AnyUUID
    ) -> TributeShopCharge | TributeError:
        return await self._handle_response(
            await self._get(
                f"/shop/charges/{self._uuid_to_str(charge_uuid)}",
            ),
            TributeShopCharge,
        )
