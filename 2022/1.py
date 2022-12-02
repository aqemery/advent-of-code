import sys

data = sys.stdin.read().split("\n\n")
groups = (g.split("\n") for g in data)
groups = sum(int(x) for x in groups)
groups = sorted(groups, reverse=True)

print("part 1:", sum(groups[0:1]))
print("part 2:", sum(groups[0:3]))
