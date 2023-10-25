import sys
from collections import deque


if __name__ == "__main__":
    data = sys.stdin.read().split("\n")
    bounds = []
    for line in data:
        line = line.split("-")
        bounds.append((int(line[0]), int(line[1])))

    bounds.sort()
    p1 = False
    q = deque(bounds)
    _, upper = q.popleft()
    total_ips = 0
    while q:
        a, b = q.popleft()
        if a <= upper + 1:
            upper = max(upper, b)
        else:
            if not p1:
                print("part 1:", upper + 1)
                p1 = True
            total_ips += a - upper - 1
            upper = b

    print("part 2:", total_ips)
