import sys
from functools import cache


def north_load(round):
    return sum(height - y for _, y in list(round))


def in_bounds(x, y):
    return 0 <= x < width and 0 <= y < height


sorts = {
    (0, -1): lambda p: p[1],
    (-1, 0): lambda p: p[0],
    (0, 1): lambda p: -p[1],
    (1, 0): lambda p: -p[0],
}


@cache
def move(round, direction):
    dx, dy = direction
    moving = True
    round = list(round)
    while moving:
        round.sort(key=sorts[direction])
        moving = False
        next_round = []
        for x, y in round:
            attempt = (x + dx, y + dy)
            if in_bounds(*attempt) and not attempt in cube and not attempt in round:
                moving = True
                next_round.append(attempt)
            else:
                next_round.append((x, y))
        round = next_round
    return frozenset(round)


def part1(round):
    return north_load(move(round, (0, -1)))


def part2(round):
    cycles = 1_000_000_000
    seen = set()
    check = None
    check_index = None
    while cycles > 0:
        for dir in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            round = move(round, dir)
        if round == check:
            jump = check_index - cycles
            cycles = cycles % jump
        if not check and round in seen:
            check = round
            check_index = cycles
        seen.add(round)
        cycles -= 1
    return north_load(round)


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    round = []
    cube = set()
    height = len(d)
    width = len(d[0])
    for y, line in enumerate(d):
        for x, c in enumerate(line):
            if c == "#":
                cube.add((x, y))
            elif c == "O":
                round.append((x, y))

    round = frozenset(round)
    print("part 1:", part1(round))
    print("part 2:", part2(round))
