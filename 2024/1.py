import sys
data = sys.stdin.read().split("\n")
first = sorted(int(l.split("   ")[0]) for l in data)
second = sorted(int(l.split("   ")[1]) for l in data)
print("part 1:", sum(abs(a - b) for a, b in zip(first, second)))
print("part 2:", sum(a * second.count(a) for a in first))
