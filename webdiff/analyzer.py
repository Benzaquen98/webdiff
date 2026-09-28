from webdiff.assets import extract_assets
from webdiff.crawler import fetch_page
from webdiff.fingerprint import fingerprint_asset


def analyze_site(url):
    response = fetch_page(url)
    assets = extract_assets(response.text, response.url)

    javascript_fingerprints = []

    for asset_url in assets["javascript"]:
        fingerprint = fingerprint_asset(asset_url, fetch_page)
        javascript_fingerprints.append(fingerprint)

    css_fingerprints = []

    for asset_url in assets["css"]:
        fingerprint = fingerprint_asset(asset_url, fetch_page)
        css_fingerprints.append(fingerprint)

    return {
        "url": response.url,
        "status_code": response.status_code,
        "assets": assets,
        "javascript_fingerprints": javascript_fingerprints,
        "css_fingerprints": css_fingerprints,
    }
