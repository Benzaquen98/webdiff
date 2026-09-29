from webdiff.cli import format_similarity


def test_format_similarity_with_value():
    assert format_similarity(100.0) == "100.0%"


def test_format_similarity_with_none():
    assert format_similarity(None) == "N/A"
