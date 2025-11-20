from collections import defaultdict

def parse(filename):
    with open(filename) as f:
        foods = []
        for line in f:
            parts = line.strip().split(' (contains ')
            ingredients = set(parts[0].split())
            allergens = set(parts[1][:-1].split(', ')) if len(parts) > 1 else set()
            foods.append((ingredients, allergens))
    return foods

def solve(foods):
    # Find possible ingredients for each allergen
    allergen_candidates = {}
    all_ingredients = []

    for ingredients, allergens in foods:
        all_ingredients.extend(ingredients)
        for allergen in allergens:
            if allergen not in allergen_candidates:
                allergen_candidates[allergen] = ingredients.copy()
            else:
                allergen_candidates[allergen] &= ingredients

    # Find definite mappings
    allergen_to_ingredient = {}
    while len(allergen_to_ingredient) < len(allergen_candidates):
        for allergen, candidates in allergen_candidates.items():
            remaining = candidates - set(allergen_to_ingredient.values())
            if len(remaining) == 1:
                allergen_to_ingredient[allergen] = remaining.pop()

    # Part 1: Count ingredients that can't contain allergens
    dangerous = set(allergen_to_ingredient.values())
    safe_count = sum(1 for ing in all_ingredients if ing not in dangerous)

    # Part 2: Canonical dangerous ingredient list
    sorted_allergens = sorted(allergen_to_ingredient.keys())
    canonical = ','.join(allergen_to_ingredient[a] for a in sorted_allergens)

    return safe_count, canonical

if __name__ == '__main__':
    foods = parse('/Users/adamemery/advent-of-code/2020/input21')
    p1, p2 = solve(foods)
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
