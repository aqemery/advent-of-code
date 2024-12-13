import sys

raw_in = sys.stdin.read()
clean = ["Button A: X+", "Button B: X+", " Y+", "Prize: X=", " Y="]
for c in clean:
    raw_in = raw_in.replace(c, "")
machines = raw_in.split("\n\n")
machines = [x.split("\n") for x in machines]
total = 0
for a, b, c in machines:
    ax, ay = [int(v) for v in a.split(",")]
    bx, by = [int(v) for v in b.split(",")]
    cx, cy = [int(v) for v in c.split(",")]

    found = []
    for x in range(max(cx // ax, cx // bx)):
        for y in range(max(cy // ay, cy // by)):
            if ax * x + bx * y == cx and ay * x + by * y == cy:
                found.append(x * 3 + y)

    if found:
        total += min(found)
print(total)
