#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ./playwright_request/_builder.py

from __future__ import annotations

import dataclasses
import typing
from dataclasses import field

from playwright._impl._api_structures import FilePayload

__all__ = ["Builder"]


@dataclasses.dataclass
class _Builder:
    url: str = field(default_factory=str)
    params: typing.Optional[typing.Dict[str, typing.Union[str, float, bool]]] = None
    method: typing.Optional[str] = "get"
    headers: typing.Optional[typing.Dict[str, str]] = None
    data: typing.Optional[typing.Union[typing.Any, str, bytes]] = None
    form: typing.Optional[typing.Dict[str, typing.Union[str, float, bool]]] = None
    multipart: typing.Dict[
        str, typing.Union[bytes, bool, float, str, FilePayload]
    ] = field(default_factory=dict)
    timeout: typing.Optional[float] = None
    fail_on_status_code: typing.Optional[bool] = None
    ignore_https_errors: typing.Optional[bool] = None
    max_redirects: typing.Optional[int] = None


class Builder:
    _builder: _Builder

    def __init__(self):
        self._builder = _Builder()

    def __repr__(self) -> str:
        return "%s: %s" % (self.__class__.__qualname__, str(self._asdict()))

    @staticmethod
    def __error__(expect, received) -> typing.NoReturn:
        msg = "Parameter type expected: '%s', received '%s'" % (expect, received)
        raise ValueError(msg)

    def _asdict(self) -> dict:
        return dataclasses.asdict(self._builder)

    def url(self, _str: str) -> Builder:
        self._builder.url = str(_str)
        return self

    def params(
        self, _dict: typing.Dict[str, typing.Union[str, float, bool]]
    ) -> Builder:
        if not isinstance(_dict, typing.Dict):
            return self.__error__(typing.Dict, type(_dict))

        self._builder.params = {**(self._builder.params or {}), **_dict}
        return self

    def method(self, _str: str) -> Builder:
        if not isinstance(_str, str):
            return self.__error__(str, type(_str))
        self._builder.method = str(_str)
        return self

    def headers(self, _dict: typing.Dict[str, str]) -> Builder:
        if not isinstance(_dict, typing.Dict):
            return self.__error__(typing.Dict, type(_dict))

        self._builder.headers = {**(self._builder.headers or {}), **_dict}
        return self

    def data(self, _any: typing.Union[typing.Any, str, bytes]) -> Builder:
        self._builder.data = _any
        return self

    def form(self, _dict: typing.Dict[str, typing.Union[str, float, bool]]) -> Builder:
        if not isinstance(_dict, typing.Dict):
            return self.__error__(typing.Dict, type(_dict))

        self._builder.form = {**(self._builder.form or {}), **_dict}
        return self

    def multipart(
        self,
        _dict: typing.Dict[str, typing.Union[bytes, bool, float, str, FilePayload]],
    ) -> Builder:
        if not isinstance(_dict, typing.Dict):
            return self.__error__(typing.Dict, type(_dict))

        self._builder.multipart = {**(self._builder.multipart or {}), **_dict}
        return self

    def timeout(self, _milliseconds: float) -> Builder:
        self._builder.timeout = float(_milliseconds)
        return self

    def fail_on_status_code(self, _bool: bool = True) -> Builder:
        self._builder.fail_on_status_code = bool(_bool)
        return self

    def ignore_https_errors(self, _bool: bool = True) -> Builder:
        self._builder.ignore_https_errors = bool(_bool)
        return self

    def max_redirects(self, _int: int) -> Builder:
        self._builder.max_redirects = int(_int)
        return self

    def delete(self, _url: str) -> Builder:
        self._builder.url = str(_url)
        self._builder.method = "delete"
        return self

    def get(self, _url: str) -> Builder:
        self._builder.url = str(_url)
        self._builder.method = "get"
        return self

    def head(self, _url: str) -> Builder:
        self._builder.url = str(_url)
        self._builder.method = "head"
        return self

    def patch(self, _url: str) -> Builder:
        self._builder.url = str(_url)
        self._builder.method = "patch"
        return self

    def put(self, _url: str) -> Builder:
        self._builder.url = str(_url)
        self._builder.method = "put"
        return self

    def post(self, _url: str) -> Builder:
        self._builder.url = str(_url)
        self._builder.method = "post"
        return self

    def reset(self) -> Builder:
        for field in dataclasses.fields(self._builder):
            setattr(self, field.name, field.default)
        return self

    def create_request(self) -> typing.Any:
        raise NotImplemented
