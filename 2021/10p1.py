import sys
from collections import deque

pop = {')':('(', 3), ']':('[', 57), '}':('{', 1197), '>':('<', 25137)}

def error_value(line):
  stack = deque()
  for c in line:
    if c in pop:
      open, v = pop[c]
      if not stack or stack.pop() != open:
        return v
    else:
      stack.append(c)
  return 0

print(sum([error_value(l) for l in sys.stdin.read().split('\n')]))
