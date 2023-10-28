import sys
from collections import deque


def parse_programs(data):
    programs = {}
    for line in data:
        line = line.replace(" <-> ", " ").replace(",", " ")
        id, *pipes = [int(n) for n in line.split()]
        programs[id] = pipes

    return programs


def part1(data):
    programs = parse_programs(data)

    visited = set()
    q = deque([0])
    while q:
        p = q.popleft()
        if p in visited:
            continue
        visited.add(p)
        q.extend(programs[p])
    return len(visited)


def part2(data):
    programs = parse_programs(data)
    groups = set()
    for program in programs:
        visited = set()
        q = deque([program])
        while q:
            p = q.popleft()
            if p in visited:
                continue
            visited.add(p)
            q.extend(programs[p])
        groups.add(frozenset(visited))
    return len(groups)


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
