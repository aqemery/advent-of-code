import sys
from itertools import combinations
from math import prod


def solve(data, groups = 3):
    packages = [int(l) for l in data]
    balance_target = sum(packages) // groups

    for num_packages in range(len(packages)//groups):
        for combo in combinations(packages, num_packages):
            if sum(combo) == balance_target:
                return prod(combo)


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", solve(d, groups=3))
    print("part 2:", solve(d, groups=4))
