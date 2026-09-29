from webdiff.comparator import find_matching_assets


def test_matching_assets_are_detected():
    assets_a = [
        {
            "url": "https://a.example/app.js",
            "sha256": "ABC123",
        }
    ]

    assets_b = [
        {
            "url": "https://b.example/main.js",
            "sha256": "ABC123",
        }
    ]

    result = find_matching_assets(assets_a, assets_b)

    assert result == [
        {
            "asset_a": "https://a.example/app.js",
            "asset_b": "https://b.example/main.js",
            "sha256": "ABC123",
        }
    ]


def test_non_matching_assets_return_empty_list():
    assets_a = [
        {
            "url": "https://a.example/app.js",
            "sha256": "ABC123",
        }
    ]

    assets_b = [
        {
            "url": "https://b.example/app.js",
            "sha256": "XYZ789",
        }
    ]

    result = find_matching_assets(assets_a, assets_b)

    assert result == []

def test_empty_asset_lists_return_empty_list():
    assets_a = []
    assets_b = []

    result = find_matching_assets(assets_a, assets_b)

    assert result == []
