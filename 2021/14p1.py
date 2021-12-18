import sys
from collections import Counter

polymer, pairs = sys.stdin.read().split("\n\n")
rules = {a: b for a, b in [p.split(" -> ") for p in pairs.split("\n")]}

for _ in range(10):
    np = polymer[0]
    for i in range(len(polymer) - 1):
        adj = polymer[i : i + 2]
        if n := rules.get(adj):
            np += n
        np += adj[-1]
    polymer = np

com = Counter(polymer).most_common()
print(com[0][1] - com[-1][1])
