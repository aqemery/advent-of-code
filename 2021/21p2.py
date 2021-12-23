import sys
from dataclasses import dataclass
from functools import cache
from collections import deque

pos = tuple(int(l.split()[-1]) for l in sys.stdin.read().split("\n"))
r = range(1, 4)
uni_rolls = [a + b + c for a in r for b in r for c in r]


@dataclass(frozen=True)
class game:
    pos: list
    score: list
    turn: int


@cache
def play_game(gg):
    winners = [0, 0]
    p1w, p2w = winners

    q = deque()
    t = gg.turn
    for roll in uni_rolls:
        cur_pos = gg.pos[t]
        cur_score = gg.score[t]
        ep = 1 + (cur_pos + roll - 1) % 10
        new_score = cur_score + ep
        if new_score >= 21:
            winners[t] += 1
        else:
            cp = list(gg.pos)
            cs = list(gg.score)
            cs[t] = new_score
            cp[t] = ep
            q.append(game(tuple(cp), tuple(cs), int(not t)))

    p1w, p2w = winners
    while q:
        p1, p2 = play_game(q.popleft())
        p1w += p1
        p2w += p2

    return p1w, p2w


print(max(play_game(game(pos, (0, 0), 0))))
