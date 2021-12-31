import sys

code = [9] * 14
cmds = [line.split() for line in sys.stdin.read().split("\n")]

stack = []
for i in range(14):
    div, chk, add = map(int, [cmds[i * 18 + x][-1] for x in [4, 5, 15]])
    if div == 1:
        stack.append((i, add))
    elif div == 26:
        j, add = stack.pop()
        code[i] = code[j] + add + chk
        if code[i] > 9:
            code[j] -= code[i] - 9
            code[i] = 9
        if code[i] < 1:
            code[j] += 1 - code[i]
            code[i] = 1

print("".join(map(str, code)))
