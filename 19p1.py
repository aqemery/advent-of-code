import sys
from collections import deque

r,m =  sys.stdin.read().split('\n\n')
rules = r.replace('"', '').split('\n')
messages = m.split('\n')

tree = {}
for r in rules:
  k, v = r.split(': ')
  tree[k] = [s.split()  for s in v.split(' | ')]

def check(message, current=tree['0'], build=''):
  for option in current:
    if o := check_option(option, message, build):
      return o
  return False

def check_option(option, message, build):
  for key in option:
    try:
      if s := check(message, tree[key], build):
        build = s
        if not message.startswith(build):
          return False
      else:
        return False
    except KeyError:
      build += key
      if not message.startswith(build):
        return False
      return build
  return build

print(sum([True for m in messages if check(m) == m]))
