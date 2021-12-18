import sys

lines = sys.stdin.read().split("\n")
grid = {(x, y): int(v) for y, row in enumerate(lines) for x, v in enumerate(row)}
r = range(-1, 2)
around = [(x, y) for x in r for y in r if (x, y) != (0, 0)]

flash_count = 0


def flash(pos):
    flashed.add(pos)
    checks = [tuple(sum(z) for z in zip(pos, a)) for a in around]
    for c in checks:
        if c not in flashed:
            try:
                v = grid[c]
                grid[c] += 1
                if v >= 9:
                    flash(c)
            except KeyError:
                pass


for _ in range(100):
    flashed = set()
    grid = {k: v + 1 for k, v in grid.items()}
    [flash(k) for k, v in grid.items() if k not in flashed and v > 9]
    for k in flashed:
        grid[k] = 0
    flash_count += len(flashed)

print(flash_count)
