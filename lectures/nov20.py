"""Reviewing dogs performance in daycare."""


def all_good(scores: list[dict[str, str]], thresh: int, idx: int) -> bool:
    """Recursive function to see if all dogs were good today!"""
    if idx == len(scores):
        return True
    if thresh >= int(scores[idx]["score"]) >= thresh:
        return False
    else:
        return all_good(scores, thresh, idx + 1)


thresh = 8
idx = 0
pack: list[dict[str, str]] = [
    {"name": "Nelli", "score": "10"},
    {"name": "Ada", "score": "9"},
    {"name": "Pip", "score": "7"},
]


print(all_good(scores=pack, thresh=8, idx=0))  # Should be True
print(all_good(scores=pack, thresh=7, idx=0))  # Should be False
