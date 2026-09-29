import argparse

from webdiff.comparator import compare_sites
from webdiff.crawler import FetchError

def format_similarity(value):
    if value is None:
        return "N/A"

    return f"{value}%"

def main():
    parser = argparse.ArgumentParser(
        description="Compare public web assets between two websites."
    )
    parser.add_argument(
        "url_a",
        help="First website URL."
    )

    parser.add_argument(
        "url_b",
        help="Second website URL."
    )
    args = parser.parse_args()
    try:
        result = compare_sites(args.url_a, args.url_b)
    except FetchError as error:
        parser.exit(1, f"WebDiff error: {error}\n")
    print()
    print("WebDiff")
    print("=======")
    print()
    print(f"Site A: {result['site_a']['url']}")
    print(f"Site B: {result['site_b']['url']}")
    print()
    print("Assets discovered")
    print("-----------------")
    print(
        f"JavaScript A: "
        f"{len(result['site_a']['javascript_fingerprints'])}"
    )
    print(
        f"JavaScript B: "
        f"{len(result['site_b']['javascript_fingerprints'])}"
    )
    print(
        f"CSS A: "
        f"{len(result['site_a']['css_fingerprints'])}"
    )
    print(
        f"CSS B: "
        f"{len(result['site_b']['css_fingerprints'])}"
    )
    print()
    print("Similarity")
    print("----------")

    javascript_similarity = result["similarity"]["javascript"]
    css_similarity = result["similarity"]["css"]
    overall_similarity = result["similarity"]["overall"]

    print(f"JavaScript: {format_similarity(javascript_similarity)}")
    print(f"CSS: {format_similarity(css_similarity)}")
    print(f"Overall: {format_similarity(overall_similarity)}")
    print()
    print("Matching assets")
    print("---------------")

    for match in result["matches"]["javascript"]:
        print("[JavaScript]")
        print(f"  Site A: {match['asset_a']}")
        print(f"  Site B: {match['asset_b']}")
        print(f"  SHA-256: {match['sha256']}")

    for match in result["matches"]["css"]:
        print("[CSS]")
        print(f"  Site A: {match['asset_a']}")
        print(f"  Site B: {match['asset_b']}")
        print(f"  SHA-256: {match['sha256']}")

if __name__ == "__main__":
    main()
