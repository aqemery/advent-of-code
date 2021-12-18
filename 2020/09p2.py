import sys

pre = 25
code = list(map(int, sys.stdin.readlines()))


def part1():
    for i, num in enumerate(code[pre:]):
        before = set(code[i : i + pre])
        for b in before:
            if num - b in before:
                break
        else:
            return num


target = part1()

l = len(code)
for i in range(l):
    for j in range(i, l):
        sub = code[i:j]
        s = sum(sub)
        if s > target:
            break
        elif s == target:
            print(min(sub) + max(sub))
            quit()
