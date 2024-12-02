import sys

data = sys.stdin.read().split("\n")

first = sorted(int(l.split("   ")[0]) for l in data)
second = sorted(int(l.split("   ")[1]) for l in data)

p1 = 0
for a, b in zip(first, second):
    p1 += abs(a - b)

print("part 1:", p1)

p2 = 0
for a in first:
    p2 += a * second.count(a)

print("part 2:", p2)
