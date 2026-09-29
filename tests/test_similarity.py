from webdiff.similarity import calculate_similarity


def test_identical_assets_have_100_percent_similarity():
    assets_a = [
        {"sha256": "A"},
        {"sha256": "B"},
    ]

    assets_b = [
        {"sha256": "A"},
        {"sha256": "B"},
    ]

    assert calculate_similarity(assets_a, assets_b) == 100.0


def test_different_assets_have_0_percent_similarity():
    assets_a = [
        {"sha256": "A"},
        {"sha256": "B"},
    ]

    assets_b = [
        {"sha256": "C"},
        {"sha256": "D"},
    ]

    assert calculate_similarity(assets_a, assets_b) == 0.0

def test_partially_matching_assets_have_50_percent_similarity():
    assets_a = [
        {"sha256": "A"},
        {"sha256": "B"},
        {"sha256": "C"},
    ]

    assets_b = [
        {"sha256": "B"},
        {"sha256": "C"},
        {"sha256": "D"},
    ]

    assert calculate_similarity(assets_a, assets_b) == 50.0

def test_empty_assets_return_none():
    assets_a = []
    assets_b = []

    assert calculate_similarity(assets_a, assets_b) is None
