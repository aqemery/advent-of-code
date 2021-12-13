import sys

dots, folds = sys.stdin.read().split('\n\n')
dots = set(tuple(int(c) for c in d.split(',')) for d in dots.split('\n'))

for f in folds.split('\n'):
  v = int(f.split('=')[-1])
  if 'x' in f:
    dots = set((i-(i-v)*2, j) if i >= v else (i,j) for i, j in dots)
  else:
    dots = set((i, j-(j-v)*2) if j >= v else (i,j) for i, j in dots)

for y in range(max(dots, key=lambda x:x[1])[1]+1):
  for x in range(max(dots)[0]+1):
    print('*' if (x,y) in dots else ' ', end='')
  print()
