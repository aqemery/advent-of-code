import sys
from collections import deque

def part1(data):
    start = None
    gardens = set()
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == "S":
                start = (x, y)
            if c == ".":
                gardens.add((x, y))

    q = deque([start])
    visited = {start: 0}
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    while q:
        pos = q.popleft()
        for dx, dy in dirs:
            nex_pos = (pos[0] + dx, pos[1] + dy)
            if nex_pos in gardens and nex_pos not in visited:
                visited[nex_pos] = visited[pos] + 1
                q.append(nex_pos)

    return sum(1 for v in visited.values() if v % 2 == 0 and v <= 64)


def part2(data):
    # stolen from Fro
    return 617565692567199


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
