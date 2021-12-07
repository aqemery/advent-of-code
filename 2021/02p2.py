import sys

depth = 0
horizontal = 0
aim = 0

def move_aim(x):
  global aim
  aim += x

def move_depth(x):
  global depth
  depth += x

def move_horizontal(x):
  global horizontal, depth
  horizontal += x
  depth += x * aim

fncs = {
  'forward': lambda x: move_horizontal(x),
  'up': lambda x: move_aim(-x),
  'down': lambda x: move_aim(x)
}

for l in sys.stdin.readlines():
  k,v = l.split()
  fncs[k](int(v))

print(depth*horizontal)
