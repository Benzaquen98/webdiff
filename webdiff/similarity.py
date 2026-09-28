def calculate_similarity(assets_a, assets_b):
    hashes_a = {asset["sha256"] for asset in assets_a}
    hashes_b = {asset["sha256"] for asset in assets_b}

    union = hashes_a | hashes_b
    intersection = hashes_a & hashes_b

    if not union:
        return None

    similarity = len(intersection) / len(union) * 100

    return round(similarity, 2)

def calculate_overall_similarity(*scores):
    valid_scores = [score for score in scores if score is not None]

    if not valid_scores:
        return None

    overall = sum(valid_scores) / len(valid_scores)

    return round(overall, 2)
