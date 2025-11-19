import re

data = open("/Users/adamemery/advent-of-code/2018/input16").read().split("\n\n\n")
samples = [
    (s[0], s[1], s[2])
    for s in [
        [list(map(int, re.findall(r"\d+", x))) for x in s.split("\n")]
        for s in data[0].split("\n\n")
    ]
]
program = [list(map(int, l.split())) for l in data[1].strip().split("\n") if l]
ops = [
    lambda r, a, b, c, f=f: r.__setitem__(c, f(r, a, b))
    for f in [
        lambda r, a, b: r[a] + r[b],
        lambda r, a, b: r[a] + b,
        lambda r, a, b: r[a] * r[b],
        lambda r, a, b: r[a] * b,
        lambda r, a, b: r[a] & r[b],
        lambda r, a, b: r[a] & b,
        lambda r, a, b: r[a] | r[b],
        lambda r, a, b: r[a] | b,
        lambda r, a, b: r[a],
        lambda r, a, b: a,
        lambda r, a, b: int(a > r[b]),
        lambda r, a, b: int(r[a] > b),
        lambda r, a, b: int(r[a] > r[b]),
        lambda r, a, b: int(a == r[b]),
        lambda r, a, b: int(r[a] == b),
        lambda r, a, b: int(r[a] == r[b]),
    ]
]
test = lambda before, instr, after, op: (r := before[:], op(r, *instr[1:]), r == after)[
    2
]
print("Part 1:", sum(sum(test(b, i, a, op) for op in ops) >= 3 for b, i, a in samples))
possible = {n: set(ops) for n in range(16)}
[
    possible[i[0]].discard(op)
    for b, i, a in samples
    for op in ops
    if not test(b, i, a, op)
]
mapping = {}
while len(mapping) < 16:
    [
        mapping.__setitem__(n, op := possible[n].pop())
        or [possible[x].discard(op) for x in possible]
        for n in possible
        if n not in mapping and len(possible[n]) == 1
    ]
regs = [0] * 4
[mapping[i[0]](regs, *i[1:]) for i in program]
print("Part 2:", regs[0])
