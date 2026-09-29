from webdiff.analyzer import analyze_site


class FakeResponse:
    url = "https://example.com/"
    status_code = 200
    text = """
    <html>
        <head>
            <link rel="stylesheet" href="/css/main.css">
        </head>
        <body>
            <script src="/js/app.js"></script>
        </body>
    </html>
    """


def test_analyze_site(monkeypatch):
    def fake_fetch_page(url):
        return FakeResponse()

    def fake_fingerprint_asset(url, fetch_function):
        return {
            "url": url,
            "status_code": 200,
            "size": 100,
            "sha256": "ABC123",
        }

    monkeypatch.setattr(
        "webdiff.analyzer.fetch_page",
        fake_fetch_page,
    )

    monkeypatch.setattr(
        "webdiff.analyzer.fingerprint_asset",
        fake_fingerprint_asset,
    )

    result = analyze_site("https://example.com")

    assert result["url"] == "https://example.com/"
    assert result["status_code"] == 200

    assert result["assets"]["javascript"] == [
        "https://example.com/js/app.js"
    ]

    assert result["assets"]["css"] == [
        "https://example.com/css/main.css"
    ]

    assert result["javascript_fingerprints"][0]["sha256"] == "ABC123"
    assert result["css_fingerprints"][0]["sha256"] == "ABC123"
