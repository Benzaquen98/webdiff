from webdiff.fingerprint import calculate_sha256


def test_sha256_is_calculated_correctly():
    content = b"hello world"

    result = calculate_sha256(content)

    assert result == (
        "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
    )
