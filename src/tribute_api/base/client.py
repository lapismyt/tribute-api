import logging
from types import TracebackType
from typing import Self

import aiohttp
from pydantic import HttpUrl, SecretStr

from tribute_api._types import StrInt


class TributeApiBaseClient:
    api_key: SecretStr
    base_url: str
    session: aiohttp.ClientSession | None = None

    def __init__(
        self,
        api_key: str | SecretStr,
        base_url: str,
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

    async def init(self):
        if self.session is None:
            self.session = aiohttp.ClientSession()

        if HttpUrl(self.base_url).scheme != "https":
            if self.allow_insecure:
                self.logger.warning("Using an insecure HTTP URL")
            else:
                msg = (
                    "base_url must be an HTTPS URL."
                    " Set allow_insecure=True if you want to use an HTTP URL."
                )
                raise ValueError(msg)

    async def close(self):
        if self.session is not None:
            await self.session.close()

    async def __aenter__(self) -> Self:
        await self.init()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.close()

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            "(api_key={self.api_key}, base_url={self.base_url})"
        )

    def __str__(self) -> str:
        return repr(self)

    def _get_url(self, path: str) -> str:
        return f"{self.base_url.rstrip('/')}{path}"

    async def _request(
        self,
        method: str,
        path: str,
        params: dict[str, StrInt | None] | None = None,
        json: dict | None = None,
        **kwargs,
    ) -> aiohttp.ClientResponse:
        if not self.session:
            msg = (
                "Client session is not initialized."
                f" Call {self.__class__.__name__}.init() first"
                " or use a context manager."
            )
            raise RuntimeError(msg)

        params: dict[str, StrInt] | None = (
            None
            if params is None
            else {k: v for k, v in params.items() if v is not None}
        )

        url = self._get_url(path)
        headers = kwargs.pop("headers", {})
        headers["Api-Key"] = self.api_key.get_secret_value()
        headers["Accept"] = "application/json"
        return await self.session.request(
            method, url, headers=headers, params=params, json=json, **kwargs
        )

    async def _get(
        self, path: str, params: dict[str, StrInt | None] | None = None, **kwargs
    ) -> aiohttp.ClientResponse:
        return await self._request("GET", path, params=params, **kwargs)

    async def _post(
        self,
        path: str,
        params: dict[str, StrInt | None] | None = None,
        json: dict | None = None,
        **kwargs,
    ) -> aiohttp.ClientResponse:
        return await self._request("POST", path, params=params, json=json, **kwargs)

    async def _delete(
        self, path: str, params: dict[str, StrInt | None] | None = None, **kwargs
    ) -> aiohttp.ClientResponse:
        return await self._request("DELETE", path, params=params, **kwargs)
