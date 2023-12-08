import sys
from collections import Counter


def get_value(card):
    if val := face_vals.get(card):
        return val
    return int(card)


def hand_value(hand):
    if p2:
        non_joke = Counter(hand.replace("J", ""))
        if non_joke:
            most = non_joke.most_common()[0][0]
            hand = hand.replace("J", most)
    counts = "".join(str(v) for _, v in Counter(hand).most_common())
    for i, s in enumerate(score):
        if counts.startswith(s):
            return 6 - i
    return 0


def line_value(line):
    h, bid = line.split()
    hand = [get_value(c) for c in h]
    value = hand_value(h)
    return value, *hand, int(bid)


def solve(data):
    all_hands = sorted(line_value(l) for l in data)
    return sum(v[-1] * (i + 1) for i, v in enumerate(all_hands))


if __name__ == "__main__":
    p2 = False
    d = sys.stdin.read().split("\n")
    face = ["A", "K", "Q", "J", "T"]
    score = ["5", "4", "32", "3", "22", "2"]
    face_vals = {f: i + 10 for i, f in enumerate(face[::-1])}
    print("part 1:", solve(d))
    p2 = True
    face_vals["J"] = 1
    print("part 2:", solve(d))
