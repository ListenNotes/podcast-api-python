"""All SDK tests are offline, including authentication and HTTP errors."""

import json
import socket

import pytest
import requests


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def blocked(*args, **kwargs):
        raise AssertionError("Unit tests must never open network connections")

    monkeypatch.setattr(socket.socket, "connect", blocked)
    monkeypatch.setattr(socket.socket, "connect_ex", blocked)


@pytest.fixture
def transport(monkeypatch):
    class Transport:
        calls = None
        status = 200
        payload = {"ok": True}
        raw = None
        error = None

        def __init__(self):
            self.calls = []

        def send(self, request, **kwargs):
            self.calls.append((request, kwargs))
            if self.error:
                raise self.error
            response = requests.Response()
            response.status_code = self.status
            response.request = request
            response.url = request.url
            response.headers["X-ListenAPI-Usage"] = "42"
            response._content = (
                self.raw
                if self.raw is not None
                else json.dumps(self.payload).encode()
            )
            response.encoding = "utf-8"
            return response

    result = Transport()
    monkeypatch.setattr(
        requests.adapters.HTTPAdapter,
        "send",
        lambda adapter, request, **kwargs: result.send(request, **kwargs),
    )
    return result
