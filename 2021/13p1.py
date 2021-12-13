import sys
from collections import deque

dots, folds = sys.stdin.read().split('\n\n')
dots = set(tuple(int(c) for c in d.split(',')) for d in dots.split('\n'))
folds = [f.split()[-1] for f in folds.split('\n')]

for f in folds:
  x, y = 0, 0
  exec(f) 
  if x:
    dots = set((i-(i-x)*2, j) if i >= x else (i,j) for i, j in dots)
  else:
    dots = set((i, j-(j-y)*2) if j >= y else (i,j) for i, j in dots)
  break

print(len(dots))
