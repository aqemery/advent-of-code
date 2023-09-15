import sys
from itertools import permutations


def get_score(amounts, by_value):
    score = 1
    for bv in by_value:
        total = sum(b * v for b, v in zip(bv, amounts))
        if total <= 0:
            return 0
        score *= total
    return score


def sove(ingredients, cals=False):
    by_value = list(zip(*ingredients))

    top_score = 0
    for p in permutations(range(1, 101), int(len(ingredients))):
        if sum(p) != 100:
            continue

        if sum(v * c for v, c in zip(p, calories)) != 500 and cals:
            continue

        score = get_score(p, by_value)
        if score > top_score:
            top_score = score
    return top_score


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    ingredients = []
    calories = []
    for l in d:
        item = l.replace(",", "")
        _, _, cap, _, d, _, f, _, t, _, cal = item.split(" ")
        calories.append(int(cal))
        values = [cap, d, f, t]
        values = [int(v) for v in values]
        ingredients.append(values)

    print("part 1:", sove(ingredients))
    print("part 2:", sove(ingredients, cals=True))
