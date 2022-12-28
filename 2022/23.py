import sys
from collections import Counter, deque
from dataclasses import dataclass


north = [(-1, -1), (0, -1), (1, -1)]
south = [(-1, 1), (0, 1), (1, 1)]
east = [(1, 1), (1, 0), (1, -1)]
west = [(-1, 1), (-1, 0), (-1, -1)]


@dataclass
class Elf:
    pos: tuple
    next: tuple = None


def solve(elves, times):
    checks = deque([north, south, west, east])

    for i in range(times):
        current_elves = set(e.pos for e in elves)
        next_moves = Counter()
        for elf in elves:
            x, y = elf.pos

            close = True
            for check in checks:
                if any((x + cx, y + cy) in current_elves for cx, cy in check):
                    close = False

            if close:
                elf.next = None
                continue

            for check in checks:
                if not any((x + cx, y + cy) in current_elves for cx, cy in check):
                    cx, cy = check[1]
                    elf.next = (x + cx, y + cy)
                    next_moves[elf.next] += 1
                    break

        fail_moves = set(m for m in next_moves if next_moves[m] > 1)

        no_move = True
        for elf in elves:
            if elf.next == None or elf.next in fail_moves:
                elf.next = None
                continue
            no_move = False
            elf.pos = elf.next
            elf.next = None
        checks.rotate(-1)

        if no_move:
            return i + 1

    x_values = [e.pos[0] for e in elves]
    y_values = [e.pos[1] for e in elves]

    return (max(x_values) - min(x_values) + 1) * (
        max(y_values) - min(y_values) + 1
    ) - len(elves)


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")

    elves = []

    for y, l in enumerate(d):
        for x, c in enumerate(l):
            if c == "#":
                elves.append(Elf(pos=(x, y)))

    print("part 1:", solve(elves, 10))

    elves = []
    for y, l in enumerate(d):
        for x, c in enumerate(l):
            if c == "#":
                elves.append(Elf(pos=(x, y)))
    print("part 2:", solve(elves, 1_000_000))
