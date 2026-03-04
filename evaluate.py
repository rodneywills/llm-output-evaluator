import json
from collections import Counter


def lexical_diversity(text):
    words = text.split()
    if not words:
        return 0
    return len(set(words)) / len(words)


def keyword_relevance(text, keywords):
    words = text.lower().split()
    count = sum(word in keywords for word in words)
    return count / len(keywords) if keywords else 0


def evaluate_response(response, keywords):
    length_score = len(response.split())
    diversity_score = lexical_diversity(response)
    keyword_score = keyword_relevance(response, keywords)

    score = (
        0.4 * length_score +
        0.3 * diversity_score +
        0.3 * keyword_score
    )

    return {
        "length": length_score,
        "diversity": diversity_score,
        "keyword_relevance": keyword_score,
        "score": score
    }


def evaluate_file(path):
    with open(path) as f:
        data = json.load(f)

    keywords = data.get("keywords", [])
    responses = data.get("responses", [])

    results = []

    for r in responses:
        result = evaluate_response(r, keywords)
        results.append(result)

    return results


if __name__ == "__main__":
    import sys

    file = sys.argv[1]
    results = evaluate_file(file)

    for i, r in enumerate(results):
        print(f"Response {i+1}:", r)
