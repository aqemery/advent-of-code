import sys
from math import prod
from functools import cmp_to_key

def compare(a, b):
    match (a, b):
        case (int(), int()):
            if a < b: return 1
            elif a > b: return -1
            return 0
        case (int(), list()):
            return compare([a], b)
        case (list(), int()):
            return compare(a, [b])
        case (list(), list()):
            for i, v in enumerate(a):
                try:
                    c = compare(v, b[i])
                    if c != 0:
                        return c
                except IndexError:
                    return -1
            if len(b) > len(a):
                return 1
            return 0
            

def part1(data):
    ordered = []
    for i, d in enumerate(data):
        d = [eval(p) for p in d.split("\n")]
        c = compare(*d)
        if c > 0:
            ordered.append(i+1)
    return sum(ordered)


def part2(data):
    all = [eval(s) for d in data for s in d.split("\n")]
    add_values = [[[2]], [[6]]]
    all += add_values
    all.sort(key=cmp_to_key(compare), reverse=True)
    return prod(all.index(av) + 1 for av in add_values)


if __name__ == "__main__":
    d = sys.stdin.read().split("\n\n")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
