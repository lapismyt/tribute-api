import pytest
from aioresponses import aioresponses

from tribute_api.v1.client import TributeApiV1Client
from tribute_api.v1.exceptions import TributeApiV1Unauthorized
from tribute_api.v1.models.enums import TributeErrorCode
from tribute_api.v1.models.enums.shop import TributeBillingPeriod, TributeShopStatus


@pytest.mark.asyncio
async def test_get_shop_unauthorized():
    api_key = "invalid_api_key"
    base_url = "https://api.tribute.tg/v1"

    with aioresponses() as m:
        m.get(
            f"{base_url}/shop",
            status=401,
            payload={
                "requestId": "test-request-id",
                "code": "error_not_permitted",
                "message": "Invalid API Key",
            },
        )

        async with TributeApiV1Client(api_key=api_key, base_url=base_url) as client:
            with pytest.raises(TributeApiV1Unauthorized) as excinfo:
                await client.get_shop()

            assert excinfo.value.error_code == TributeErrorCode.NOT_PERMITTED
            assert excinfo.value.message == "Invalid API Key"


@pytest.mark.asyncio
async def test_get_shop():
    api_key = "test_api_key"
    base_url = "https://api.tribute.tg/v1"

    with aioresponses() as m:
        m.get(
            f"{base_url}/shop",
            payload={
                "userId": 123,
                "name": "My Shop",
                "link": "myshop",
                "callbackUrl": "https://example.com/webhook",
                "recurrent": True,
                "onlyStars": False,
                "status": 1,
            },
        )

        async with TributeApiV1Client(api_key=api_key, base_url=base_url) as client:
            shop = await client.get_shop()

            assert shop.user_id == 123
            assert shop.name == "My Shop"
            assert shop.status == TributeShopStatus.ACTIVE


@pytest.mark.asyncio
async def test_get_shop_orders():
    api_key = "test_api_key"
    base_url = "https://api.tribute.tg/v1"

    with aioresponses() as m:
        m.get(
            f"{base_url}/shop/orders",
            payload=[
                {
                    "uuid": "550e8400-e29b-41d4-a716-446655440000",
                    "amount": 1000,
                    "currency": "rub",
                    "title": "Test Order",
                    "description": "Test Description",
                    "status": "paid",
                    "email": "test@example.com",
                    "successUrl": "https://example.com/success",
                    "failureUrl": "https://example.com/fail",
                    "paymentUrl": "https://example.com/pay",
                    "createdAt": "2023-01-01T00:00:00Z",
                    "period": "onetime",
                }
            ],
        )

        async with TributeApiV1Client(api_key=api_key, base_url=base_url) as client:
            orders = await client.get_shop_orders()

            assert len(orders) == 1
            assert str(orders[0].uuid) == "550e8400-e29b-41d4-a716-446655440000"
            assert orders[0].amount == 1000
            assert orders[0].period == TributeBillingPeriod.ONETIME
