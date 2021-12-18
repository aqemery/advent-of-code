import math
import itertools

moons = []
while True:
    try:
        list(map(exec, input().strip("<>").split(", ")))
        m = {"pos": [x, y, z], "vel": [0] * 3}
        moons.append(m)
    except EOFError:
        break

pairs = list(itertools.combinations(moons, 2))

for _ in range(1000):
    for p in pairs:
        a, b = p
        for i in range(3):
            ap = a["pos"][i]
            bp = b["pos"][i]
            if ap > bp:
                a["vel"][i] -= 1
                b["vel"][i] += 1
            elif ap < bp:
                a["vel"][i] += 1
                b["vel"][i] -= 1
    for m in moons:
        m["pos"] = [sum(i) for i in zip(m["pos"], m["vel"])]

energy = [sum(map(abs, m["pos"])) * sum(map(abs, m["vel"])) for m in moons]
print(sum(energy))
