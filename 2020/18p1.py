import sys

out = 0

for line in sys.stdin.readlines():
    line = line.strip().replace(" ", "")
    stack = []
    op = None
    val = None

    for c in line:
        if c == "(":
            stack.append((val, op))
            op = None
            val = None
        elif c == ")":
            try:
                s_val, s_op = stack.pop()
                val = str(eval(s_val + s_op + val))
            except TypeError:
                pass
        elif c in ["+", "*"]:
            op = c
        elif val and op:
            val = str(eval(val + op + c))
            op = None
        else:
            val = c
    out += int(val)
print(out)
