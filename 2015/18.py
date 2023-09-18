import sys


def solve(data, times=100, part2=False):
    on = set()
    for y, d in enumerate(data):
        for x, c in enumerate(d):
            if c == "#":
                on.add((x, y))

    size = len(data) - 1

    for _ in range(times):
        next_on = set()
        for y in range(len(data)):
            for x in range(len(data[0])):
                around = sum(
                    (x + dx, y + dy) in on
                    for dx, dy in [
                        (0, 1),
                        (0, -1),
                        (1, 0),
                        (-1, 0),
                        (1, 1),
                        (-1, 1),
                        (-1, -1),
                        (1, -1),
                    ]
                )
                if (x, y) in on and around in [2, 3]:
                    next_on.add((x, y))
                elif (x, y) not in on and around == 3:
                    next_on.add((x, y))
        on = next_on

        if part2:
            on.update([(0, 0), (0, size), (size, 0), (size, size)])

    return len(next_on)


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", solve(d))
    print("part 2:", solve(d, part2=True))
