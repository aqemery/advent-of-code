import sys
from collections import deque

lines = sys.stdin.read().split("\n")
caves = {}


def add_edge(a, b):
    if a in caves:
        caves[a].append(b)
    else:
        caves[a] = [b]


for l in lines:
    a, b = l.split("-")
    add_edge(a, b)
    add_edge(b, a)

q = deque([("start", set(), True)])
paths = 0
while q:
    room, visited, twice = q.popleft()
    if room == "end":
        paths += 1
        continue
    if not room.isupper():
        visited = set(visited)
        visited.add(room)

    for r in caves[room]:
        if r in visited and twice and r not in ["start", "end"]:
            q.append((r, visited, False))
        elif r not in visited:
            q.append((r, visited, twice))

print(paths)
