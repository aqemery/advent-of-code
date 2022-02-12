import sys
from collections import defaultdict
from itertools import permutations


def solve(data, me=False):
    names = set()
    happiness = defaultdict(int)
    for l in data:
        n1, _, t, v, _, _, _, _, _, _, n2 = l[:-1].split()
        v = int(v)
        happiness[(n1, n2)] = v if t == "gain" else -v
        names.add(n1)
    if me:
        names.add("me")

    t_max = 0
    for p in permutations(names):
        t = 0
        for i, n1 in enumerate(p):
            n2 = p[i - 1]
            t += happiness[(n1, n2)]
            t += happiness[(n2, n1)]
        if t > t_max:
            t_max = t

    return t_max


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", solve(d))
    print("part 2:", solve(d, me=True))
