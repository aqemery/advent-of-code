import sys

data = sys.stdin.read().split("\n\n")
groups = (sum(int(x) for x in g.split("\n")) for g in data)
groups = sorted(groups, reverse=True)

print("part 1:", sum(groups[0:1]))
print("part 2:", sum(groups[0:3]))
