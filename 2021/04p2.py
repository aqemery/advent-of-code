import sys

boards = sys.stdin.read().split("\n\n")
calls = boards[0].split(",")


def check_set(e):
    found = 0
    for j, c in enumerate(calls):
        if c in e:
            found += 1
        if found == 5:
            return j


last_call = 0
loser = None
for i, b in enumerate(boards[1:]):
    rows = [l.split() for l in b.split("\n")]
    cols = list(zip(*rows))
    win_call = min([check_set(e) for e in rows + cols])
    if last_call < win_call:
        last_call = win_call
        loser = i

w_board_values = [v for l in boards[loser + 1].split("\n") for v in l.split()]
unmarked = sum([int(v) for v in w_board_values if v not in calls[: last_call + 1]])
print(unmarked * int(calls[last_call]))
