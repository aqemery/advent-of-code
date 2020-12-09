import sys

pre = 25
code = list(map(int, sys.stdin.readlines()))
for i, num in enumerate(code[pre:]):
  before = set(code[i:i+pre])
  for b in before:
    if num - b in before:
      break
  else:
    print(num)
    break
