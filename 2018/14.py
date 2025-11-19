#!/usr/bin/env python3
"""Advent of Code 2018 Day 14: Chocolate Charts"""

def solve(input_num):
    recipes = [3, 7]
    elf1 = 0
    elf2 = 1

    input_str = str(input_num)
    input_len = len(input_str)
    input_list = [int(d) for d in input_str]

    part1 = None
    part2 = None

    # We need at least input_num + 10 recipes for part 1
    # For part 2, we need to find when the sequence appears

    while part1 is None or part2 is None:
        # Create new recipes
        total = recipes[elf1] + recipes[elf2]
        if total >= 10:
            recipes.append(total // 10)
            # Check for part 2 after adding first digit
            if part2 is None and len(recipes) >= input_len:
                if recipes[-input_len:] == input_list:
                    part2 = len(recipes) - input_len

        recipes.append(total % 10)

        # Check for part 2 after adding second digit
        if part2 is None and len(recipes) >= input_len:
            if recipes[-input_len:] == input_list:
                part2 = len(recipes) - input_len

        # Move elves
        elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
        elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)

        # Check for part 1
        if part1 is None and len(recipes) >= input_num + 10:
            part1 = ''.join(str(r) for r in recipes[input_num:input_num + 10])

    return part1, part2

if __name__ == "__main__":
    with open("/Users/adamemery/advent-of-code/2018/input14") as f:
        input_num = int(f.read().strip())

    part1, part2 = solve(input_num)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
