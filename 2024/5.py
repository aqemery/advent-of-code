import sys
from collections import defaultdict

order, lines = sys.stdin.read().split("\n\n")
order = [o.split("|") for o in order.split("\n")]
lines = [[int(v) for v in l.split(",")] for l in lines.split("\n")]


order_map = defaultdict(set)
for o in order:
    order_map[int(o[0])].add(int(o[1]))


def middle(l):
    return l[len(l) // 2]


def correct_line(l):
    new_l = []
    for v in l:
        for i in range(len(new_l) + 1):
            sub = new_l[: len(new_l) - i]
            if not order_map[v] & set(sub):
                new_l.insert(len(sub), v)
                break
    return new_l


p1 = 0
p2 = 0

for l in lines:
    for i, v in enumerate(l):
        before = set(l[:i])
        if order_map[v] & before:
            p2 += middle(correct_line(l))
            break
    else:
        p1 += middle(l)

print("part 1:", p1)
print("part 2:", p2)
