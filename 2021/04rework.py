import sys

groups = sys.stdin.read().split('\n\n')
calls = groups[0].split(',')
boards = groups[1:]

def board_value(index, turn):
  w_board_values = [v for l in boards[index].split('\n') for v in l.split()]
  unmarked = sum([int(v) for v in w_board_values if v not in calls[:turn+1]])
  return unmarked * int(calls[turn])

def get_win(b):
  rows = [list(map(calls.index,l.split())) for l in b.split('\n')]
  cols = list(zip(*rows))
  return min([max(e) for e in rows + cols])

win_turns = list(map(get_win, boards))

first = min(win_turns)
print('part 1:', board_value(win_turns.index(first), first))

last = max(win_turns)
print('part 2:', board_value(win_turns.index(last), last))
