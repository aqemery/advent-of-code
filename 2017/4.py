import sys
from collections import Counter
from itertools import permutations

def part1(data):
    return sum(1 for l in data if Counter(l.split()).most_common()[0][1] == 1)


def part2(data):
    total = 0
    lines = [l.split() for l in data if Counter(l.split()).most_common()[0][1] == 1]

    for line in lines:
        for word in line:
            checks = ["".join(p) for p in permutations(word)]
            for c in checks:
                if c == word:
                    continue
                if c in line:
                    break
            else:
                continue
            break
        else:
            total += 1

    return total


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
