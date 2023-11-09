import sys

data = sys.stdin.read().split("\n")
values = [int(n) for n in data]
out = sum(values)
print("part1:", out)

totals = []

current = 0
for v in values:
    current += v
    totals.append(current)


seen = set()
current = 0
while True:
    for v in values:
        current += v
        if current in seen:
            print("part2:", current)
            exit()
        seen.add(current)
