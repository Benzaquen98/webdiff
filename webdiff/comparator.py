from webdiff.analyzer import analyze_site
from webdiff.similarity import (
    calculate_overall_similarity,
    calculate_similarity,
)


def find_matching_assets(assets_a, assets_b):
    matches = []

    for asset_a in assets_a:
        for asset_b in assets_b:
            if asset_a["sha256"] == asset_b["sha256"]:
                matches.append({
                    "asset_a": asset_a["url"],
                    "asset_b": asset_b["url"],
                    "sha256": asset_a["sha256"],
                })

    return matches


def compare_sites(url_a, url_b):
    site_a = analyze_site(url_a)
    site_b = analyze_site(url_b)

    javascript_matches = find_matching_assets(
        site_a["javascript_fingerprints"],
        site_b["javascript_fingerprints"],
    )

    css_matches = find_matching_assets(
        site_a["css_fingerprints"],
        site_b["css_fingerprints"],
    )

    javascript_similarity = calculate_similarity(
        site_a["javascript_fingerprints"],
        site_b["javascript_fingerprints"],
    )

    css_similarity = calculate_similarity(
        site_a["css_fingerprints"],
        site_b["css_fingerprints"],
    )

    overall_similarity = calculate_overall_similarity(
        javascript_similarity,
        css_similarity,
    )

    return {
        "site_a": site_a,
        "site_b": site_b,
        "matches": {
            "javascript": javascript_matches,
            "css": css_matches,
        },
        "similarity": {
            "javascript": javascript_similarity,
            "css": css_similarity,
            "overall": overall_similarity,
        },
    }
