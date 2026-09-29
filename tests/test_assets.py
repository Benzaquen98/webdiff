from webdiff.assets import extract_scripts, extract_stylesheets


def test_extract_scripts_resolves_relative_urls():
    html = """
    <html>
        <script src="/js/app.js"></script>
        <script src="assets/main.js"></script>
    </html>
    """

    result = extract_scripts(html, "https://example.com")

    assert result == [
        "https://example.com/js/app.js",
        "https://example.com/assets/main.js",
    ]


def test_extract_stylesheets_resolves_relative_urls():
    html = """
    <html>
        <head>
            <link rel="stylesheet" href="/css/main.css">
            <link rel="stylesheet" href="assets/theme.css">
        </head>
    </html>
    """

    result = extract_stylesheets(html, "https://example.com")

    assert result == [
        "https://example.com/css/main.css",
        "https://example.com/assets/theme.css",
    ]
