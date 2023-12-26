import sys
from collections import deque
from itertools import combinations
from math import prod


data = sys.stdin.read().split("\n")
connections = set()
for l in data:
    l.replace(":", "").split()
    k, *v = l.replace(":", "").split()
    for c in v:
        connections.add(tuple(sorted([k, c])))

for wires in combinations(connections, 3):
    cons = connections.copy()
    for w in wires:
        cons.remove(w)
    out = []
    for i in range(2):
        visited = set()
        q = deque(list(cons)[0])
        while q:
            c = q.popleft()
            if c in visited:
                continue
            visited.add(c)
            for n in cons:
                if c in n:
                    q.append(n[0] if n[0] != c else n[1])
        out.append(len(visited))
        cons = set(c for c in cons if c[0] not in visited)
        cons.difference_update(visited)
        if len(cons) == 0 and len(out) == 2:
            print(prod(out))
            exit()
        if len(cons) == 0:
            break

# works for part 1 sample
# actual input is too big for this to work
# graphviz -> pdf -> slipt pdf in two -> copy all text and remove white space -> divide by 3