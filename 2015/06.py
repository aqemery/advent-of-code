import sys
from itertools import chain


def ranges(rest):
    p1, _, p2 = rest
    x1, y1 = map(int, p1.split(','))
    x2, y2 = map(int, p2.split(','))
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            yield x, y


def part1(data):
    s = 1000
    grid = [[False] * s for _ in range(s)]
    for l in data:
        match l.split():
            case ['turn', on_off, *rest]:
                on = on_off == 'on'
                for x, y in ranges(rest):
                    grid[x][y] = on
            case ['toggle', *rest]:
                for x, y in ranges(rest):
                    grid[x][y] = not grid[x][y]

    return sum(chain.from_iterable(grid))


def part2(data):
    s = 1000
    grid = [[False] * s for _ in range(s)]
    for l in data:
        match l.split():
            case ['turn', on_off, *rest]:
                on = 1 if on_off == 'on' else -1
                for x, y in ranges(rest):
                    grid[x][y] += on
                    if grid[x][y] < 0:
                        grid[x][y] = 0
            case ['toggle', *rest]:
                for x, y in ranges(rest):
                    grid[x][y] += 2

    return sum(chain.from_iterable(grid))


if __name__ == "__main__":
    d = sys.stdin.read().split('\n')
    print("part 1:", part1(d))
    print("part 2:", part2(d))
