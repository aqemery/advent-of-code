import sys

search = [2, 3, 4, 7]
lines = [[s.split() for s in l.split("|")] for l in sys.stdin.readlines()]
order = [1, 4, 7, 8, 6, 9, 0, 2, 3, 5]

rules = {
    0: lambda x: len(x) == 6 and not digits[4].issubset(x) and digits[1].issubset(x),
    1: lambda x: len(x) == 2,
    2: lambda x: len(x) == 5
    and not x.issubset(digits[6])
    and not digits[7].issubset(x),
    3: lambda x: len(x) == 5 and digits[7].issubset(x),
    4: lambda x: len(x) == 4,
    5: lambda x: len(x) == 5 and x.issubset(digits[6]),
    6: lambda x: len(x) == 6 and not digits[1].issubset(x),
    7: lambda x: len(x) == 3,
    8: lambda x: len(x) == 7,
    9: lambda x: len(x) == 6 and digits[4].issubset(x),
}

total = 0
for l in lines:
    seqen, disp = [[set(s) for s in g] for g in l]
    digits = {}

    for o in order:
        rule = rules[o]
        for s in seqen:
            if rule(s):
                digits[o] = s
                break

    displayed = [str(k) for d in disp for k, v in digits.items() if d == v]
    total += int("".join(displayed))

print(total)
