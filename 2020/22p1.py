import sys
from collections import deque

one, two = sys.stdin.read().split("\n\n")
p1 = deque(map(int, one.split()[2:]))
p2 = deque(map(int, two.split()[2:]))

while len(p1) > 0 and len(p2) > 0:
    a = p1.popleft()
    b = p2.popleft()
    if a > b:
        p1.append(a)
        p1.append(b)
    else:
        p2.append(b)
        p2.append(a)

winner = p1 if len(p1) > 0 else p2
print(sum([i * winner.pop() for i in range(1, len(winner) + 1)]))
