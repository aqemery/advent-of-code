import sys
from collections import defaultdict

d = sys.stdin.read().split("\n")

red_max = 12
green_max = 13
blue_max = 14

power = 0
total = 0
for index, line in enumerate(d):
    rgb = defaultdict(int)
    game = line.split(":")[-1]

    pulls = [p.split() for pull in game.split(";") for p in pull.split(",")]
    for pull in pulls:
        count, color = pull
        count = int(count)
        rgb[color] = max(count, rgb[color])

    if rgb["red"] <= red_max and rgb["green"] <= green_max and rgb["blue"] <= blue_max:
        total += index + 1

    power += rgb["red"] * rgb["green"] * rgb["blue"]
print("part 1:", total)
print("part 2:", power)
