import sys
from itertools import combinations


def solve(data, minimum=False):
    total = 0
    data = [int(d) for d in data]
    for i in range(len(data)):
        for c in combinations(data, i+1):
            if sum(c) == 150:
                total += 1
        if total and minimum:
            return total
    return total

if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", solve(d))
    print("part 2:", solve(d, True))
