import sys

lines = sys.stdin.read().split("\n")

pointer = 50
p1 = 0
p2 = 0
for line in lines:
    print("====", line)
    dir, *vals = line
    vals = int("".join(vals))

    crossed = 0
    for _ in range(vals):
        if dir == "L":
            pointer -= 1
        elif dir == "R":
            pointer += 1
        pointer %= 100
        if pointer == 0:
            crossed += 1
    p2 += crossed
    if pointer == 0:
        p1 += 1

print("part 1:", p1)
print("part 2:", p2)
