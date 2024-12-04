import sys

lines = sys.stdin.read().splitlines()
vertical = ["".join(z) for z in zip(*lines)]
size = len(lines) + len(lines[0]) - 1
diagonal1 = [[] for _ in range(size)]
diagonal2 = [[] for _ in range(size)]
for x, l in enumerate(lines):
    for y, c in enumerate(l):
        diagonal1[x + y].append(c)
        diagonal2[x - y].append(c)

diagonal1 = ["".join(d) for d in diagonal1]
diagonal2 = ["".join(d) for d in diagonal2]
strings = lines + vertical + diagonal1 + diagonal2

p1 = sum(s.count("XMAS") + s.count("SAMX") for s in strings)
print("p1:", p1)

p2 = 0
for x in range(1, len(lines) - 1):
    for y in range(1, len(lines[0]) - 1):
        if lines[x][y] == "A":
            x1 = lines[x - 1][y - 1] + lines[x + 1][y + 1]
            x1 = "MS" in x1 or "SM" in x1
            x2 = lines[x - 1][y + 1] + lines[x + 1][y - 1]
            x2 = "MS" in x2 or "SM" in x2
            if x1 and x2:
                p2 += 1

print("p2:", p2)
