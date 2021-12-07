import sys

depth = 0
horizontal = 0

def move_depth(x):
  global depth
  depth += x

def move_horizontal(x):
  global horizontal
  horizontal += x

fncs = {
  'forward': lambda x: move_horizontal(x),
  'up': lambda x: move_depth(-x),
  'down': lambda x: move_depth(x)
}

for l in sys.stdin.readlines():
  k,v = l.split()
  fncs[k](int(v))

print(depth*horizontal)
