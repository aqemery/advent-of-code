import sys

boards = sys.stdin.read().split('\n\n')

calls = boards[0].split(',')

max_call = len(calls)
winner = None

for i, b in enumerate(boards[1:]):
  rows = [l.split() for l in b.split('\n')]
  cols = list(zip(*rows))
  for e in rows + cols:
    found = 0
    for j, c in enumerate(calls):
      if j >= max_call:
        break
      if c in e:
        found += 1
      if found == 5:
        max_call = j
        winner = i
        break

w_board_values = [v for l in boards[winner+1].split('\n') for v in l.split()]
unmarked = sum([int(v) for v in w_board_values if v not in calls[:max_call+1]])
print(unmarked * int(calls[max_call]))
