import sys
from collections import Counter


d = sys.stdin.read().split("\n")

real_rooms = []
sectors = 0
for line in d:
    name, token = line.split("[")
    name, sector = name.rsplit("-", 1)
    name_nd = name.replace("-", "")
    token = token.replace("]", "")

    counts = Counter(name_nd)
    counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    if "".join(x[0] for x in counts[:5]) == token:
        sector_value = int(sector)
        sectors += sector_value
        real_rooms.append((name, sector_value))

print("part 1:", sectors)


def shift(c, s):
    if c == "-":
        return " "

    return chr((ord(c) - ord("a") + s) % 26 + ord("a"))


print("part 2:")
for n, s in real_rooms:
    name = "".join(shift(c, s) for c in n)
    if "north" in name:
        print(name, s)
