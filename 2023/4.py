import sys
from collections import Counter

data = sys.stdin.read().split("\n")
total = 0
more = Counter()

for index, line in enumerate(data):
    a, b = [set(l.split()) for l in line.split(": ")[-1].split("|")]
    if winners := len(a & b):
        total += 2 ** (winners - 1)
        bonus = list(range(index + 1, index + winners + 1))
        more.update(bonus * (more[index] + 1))

print("part 1:", total)
print("part 2:", sum(more.values()) + len(data))
