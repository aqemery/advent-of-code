import sys
from collections import Counter


splits = set()
current = set()
start = None
lines = sys.stdin.read().split("\n")
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "^":
            splits.add((x, y))
        elif char == "S":
            start = (x, y)


split_hits = 0
times_lines = Counter([start])
for _ in range(len(lines)):
    new_times_lines = Counter()
    for cx, cy in times_lines.keys():
        if (cx, cy + 1) in splits:
            new_times_lines[(cx + 1, cy + 1)] += times_lines[(cx, cy)]
            new_times_lines[(cx - 1, cy + 1)] += times_lines[(cx, cy)]
            split_hits += 1
        else:
            new_times_lines[(cx, cy + 1)] += times_lines[(cx, cy)]

    times_lines = new_times_lines

print("Part 1:", split_hits)

print("Part 2:", sum(times_lines.values()))
