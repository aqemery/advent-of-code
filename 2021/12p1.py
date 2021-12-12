import sys
from collections import deque

lines = sys.stdin.read().split('\n')
caves = {}

def add_edge(a,b):
  if a in caves:
    caves[a].append(b)
  else: 
    caves[a] = [b]

for l in lines:
  a, b = l.split('-')
  add_edge(a,b)
  add_edge(b,a)

q = deque([('start', set())])
paths = 0
while q:
  room, visited = q.popleft()
  if room == 'end':
    paths += 1
    continue
  if not room.isupper():
    visited = set(visited)
    visited.add(room)
  q.extend([(r, visited) for r in caves[room] if r not in visited])

print(paths)