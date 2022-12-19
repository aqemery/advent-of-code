import sys
from collections import deque

data = sys.stdin.read().split("\n")
pointer = deque()
totals = []
cur = 0
for d in data:
    match d.split():
        case ["$", "cd", ".."]:
            totals.append(cur)
            cur = pointer.pop() + cur
        case ["$", "cd", "/"]:
            pointer = deque()
        case ["$", "cd", dir]:
            pointer.append(cur)
            cur = 0
        case ["$", "ls"]:
            pass
        case ["dir", _]:
            pass
        case [size, f]:
            cur += int(size)

p1 = sum([t for t in totals if t <= 100_000])
print("part 1:", p1)

used_space = sum(pointer) + cur
to_free = 30_000_000 - (70_000_000 - used_space)

p2 = min([t for t in totals if t >= to_free])
print("part 2:", p2)
