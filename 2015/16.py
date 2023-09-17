import sys
from collections import deque
from dataclasses import dataclass

target = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

@dataclass
class Sue:
    num: int
    propties: dict


def solve(data, greater=False):
    sues = deque()
    for i, d in enumerate(data):
        d = d.replace(",", "").replace(":", "")
        _, _, *s = d.split(" ")
        propties = {}
        for x in range(0, len(s), 2):
            propties[s[x]] = int(s[x+1])
        sue = Sue(i+1, propties)
        sues.append(sue)

    maybe = []

    this_target = target.copy()
    if greater:
        this_target["cats"] += 1
        this_target["trees"] += 1
        this_target["pomeranians"] -= 2
        this_target["goldfish"] -= 2

    while sues:
        sue = sues.popleft()
        for k, v in sue.propties.items():
            if greater and k in ["cats", "trees"] and v <= target[k]:
                break
            if greater and k in ["pomeranians", "goldfish"] and v >= target[k]:
                break
            if this_target[k] != v:
                break
        else:
            maybe.append(sue)
    return maybe[0].num

if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", solve(d))
    print("part 2:", solve(d, True))
