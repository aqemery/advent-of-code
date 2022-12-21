import sys
from collections import deque


def part1(data):
    q = deque(data)
    while l := q.popleft():
        try:
            exec(l)
        except NameError:
            q.append(l)
        if "root" in locals():
            return int(locals()["root"])


def container(data, a, b, humn):
    q = deque(data)
    while l := q.popleft():
        try:
            exec(l)
        except NameError:
            q.append(l)
        if a in locals() and b in locals():
            if locals()[a] == locals()[b]:
                print("part 2:", int(humn))
                exit()
            return locals()[a] < locals()[b]


def part2(data, a, b):
    search = 1
    increase = 1_000_000_000_000

    direction = False

    while True:
        if direction == container(data, a, b, search):
            search += increase
        else:
            direction = not direction
            increase *= -0.5
            search += increase


if __name__ == "__main__":
    data = sys.stdin.read().replace(": ", " = ").split("\n")
    print("part 1:", part1(data))

    for d in data:
        if "root" in d:
            _, _, a, _, b = d.split()
            part2(data, a, b)
