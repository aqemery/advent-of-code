import sys
import re


def solve_part(r, line):
    while m := re.search(r, line):
        s = m.group()
        line = line.replace(s, str(eval(s)))
    return line


regxs = ["\d+(\+\d+)+", "\(\d+(\*\d+)+\)", "\(\d*\)"]
out = 0

for line in sys.stdin.readlines():
    line = line.strip().replace(" ", "")
    while "(" in line or "+" in line:
        for r in regxs:
            line = solve_part(r, line)
    out += eval(line)
print(out)
