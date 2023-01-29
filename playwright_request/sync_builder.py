#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ./playwright_request/sync_builder.py

from __future__ import annotations

import dataclasses
import pathlib
import typing

from playwright.sync_api import (
    APIRequestContext,
    APIResponse,
    HttpCredentials,
    Playwright,
    ProxySettings,
    StorageState,
    sync_playwright,
)

from playwright_request._builder import Builder

__all__ = ["RequestBuilder"]


class RequestBuilder(Builder):
    _playwright: typing.Optional[Playwright]
    _request_context: APIRequestContext

    def __init__(
        self,
        playwright: typing.Optional[Playwright] = None,
        *,
        base_url: typing.Optional[str] = None,
        extra_http_headers: typing.Optional[typing.Dict[str, str]] = None,
        http_credentials: typing.Optional[HttpCredentials] = None,
        ignore_https_errors: typing.Optional[bool] = None,
        proxy: typing.Optional[ProxySettings] = None,
        user_agent: typing.Optional[str] = None,
        timeout: typing.Optional[float] = None,
        storage_state: typing.Optional[
            typing.Union[StorageState, str, pathlib.Path]
        ] = None,
    ) -> None:
        self._playwright = playwright
        self._base_url = base_url
        self._extra_http_headers = extra_http_headers
        self._http_credentials = http_credentials
        self._ignore_https_errors = ignore_https_errors
        self._proxy = proxy
        self._user_agent = user_agent
        self._timeout = timeout
        self._storage_state = storage_state
        super().__init__()

    def request_context(self) -> APIRequestContext:
        if self._playwright is None or not isinstance(self._playwright, Playwright):
            self._playwright = sync_playwright().start()
        return self._playwright.request.new_context(
            base_url=self._base_url,
            extra_http_headers=self._extra_http_headers,
            http_credentials=self._http_credentials,
            ignore_https_errors=self._ignore_https_errors,
            proxy=self._proxy,
            user_agent=self._user_agent,
            timeout=self._timeout,
            storage_state=self._storage_state,
        )

    def create_request(
        self,
    ) -> typing.Callable[[typing.Optional[APIRequestContext]], APIResponse]:
        dict_ = dataclasses.asdict(self._builder)
        url = dict_.pop("url")

        def _do(context: typing.Optional[APIRequestContext] = None) -> APIResponse:
            if context is None or not isinstance(context, APIRequestContext):
                context = self.request_context()
            return context.fetch(url, **dict_)

        return _do  # `_do` is a closure

    # monkey patch
    create = create_request

    def do(self, context: typing.Optional[APIRequestContext] = None) -> APIResponse:
        _request = self.create_request()
        return _request(context)


if __name__ == "__main__":
    url = r"https://wttr.in/"

    def main() -> int:
        with sync_playwright() as p:
            builder = RequestBuilder(p, base_url=url)
            request = (
                builder.get("Amsterdam")
                .headers({"Accept-Language": "en-US"})
                .params({"format": "4"})
                .create_request()
            )

            response = request()
            print(response.text())

        return 0

    raise SystemExit(main())
