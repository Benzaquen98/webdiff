import pytest
import requests

from webdiff.crawler import FetchError, fetch_page


class FakeResponse:
    status_code = 200
    url = "https://example.com/"
    text = "Example page"


def test_fetch_page_uses_requests_get(monkeypatch):
    def fake_get(url, timeout):
        assert url == "https://example.com"
        assert timeout == 10
        return FakeResponse()

    monkeypatch.setattr("webdiff.crawler.requests.get", fake_get)

    response = fetch_page("https://example.com")

    assert response.status_code == 200
    assert response.url == "https://example.com/"
    assert response.text == "Example page"


def test_fetch_page_raises_fetch_error(monkeypatch):
    def fake_get(url, timeout):
        raise requests.ConnectionError("Connection failed")

    monkeypatch.setattr("webdiff.crawler.requests.get", fake_get)

    with pytest.raises(FetchError):
        fetch_page("https://example.invalid")
