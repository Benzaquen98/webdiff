import hashlib


def calculate_sha256(content):
    return hashlib.sha256(content).hexdigest()

def fingerprint_asset(url, fetch_function):
    response = fetch_function(url)

    return {
        "url": response.url,
        "status_code": response.status_code,
        "size": len(response.content),
        "sha256": calculate_sha256(response.content),
    }
