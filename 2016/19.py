import sys
from collections import deque

elf_count = 3004953


def round(elves):
    for i, elf in enumerate(elves):
        _, presents = elf
        if not presents:
            continue
        try:
            elves[i + 1][1] = False
        except IndexError:
            elves[0][1] = False
    return [e for e in elves if e[1]]


def part1():
    elves = [[i + 1, True] for i in range(elf_count)]
    while len(elves) > 1:
        elves = round(elves)
    return elves[0][0]


def part2():
    elves = deque(i + 1 for i in range(elf_count))
    while len(elves) > 1:
        half = (len(elves) // 2) % len(elves)
        elves.rotate(-half)
        elves.popleft()
        elves.rotate(half - 1)
    return elves.pop()


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", part1())
    print("part 2:", part2())
