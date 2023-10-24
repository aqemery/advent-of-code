from collections import deque
import hashlib


directions = {
    "U": (0, -1),
    "D": (0, 1),
    "R": (1, 0),
    "L": (-1, 0),
}

current = (0, 0, "")

paths = []
q = deque([current])
shortest = None
longest = 0
while q:
    x, y, path = q.popleft()
    if x == 3 and y == 3:
        if shortest is None:
            shortest = path
            print("part 1:", shortest)

        if len(path) > longest:
            longest = len(path)
        continue

    hash_code = f"yjjvjgan{path}".encode()
    hex = hashlib.md5(hash_code).hexdigest()[:4]
    for i, d in enumerate("UDLR"):
        if not hex[i] in "bcdef":
            continue
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            q.append((nx, ny, path + d))


print("part 2:", longest)
