"""Tests are offline unless mock-server integration tests are requested."""

import json
import socket

import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--run-integration",
        action="store_true",
        help="Run integration tests against the public Listen API mock server",
    )


def pytest_collection_modifyitems(config, items):
    if config.getoption("--run-integration"):
        return
    skip = pytest.mark.skip(
        reason="Use --run-integration to call the mock API"
    )
    for item in items:
        if item.get_closest_marker("integration"):
            item.add_marker(skip)


@pytest.fixture(autouse=True)
def no_network(monkeypatch, request):
    if request.node.get_closest_marker(
        "integration"
    ) and request.config.getoption("--run-integration"):
        return

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
