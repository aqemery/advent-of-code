import sys
from collections import  deque
from itertools import permutations

def scramble(data, word):
    scramble = list(word)
    for line in data:
        match line.split():
            case ["swap", "position", a, "with", "position", b]:
                a, b = int(a), int(b)
                scramble[a], scramble[b] = scramble[b], scramble[a]
            case ["swap", "letter", a, "with", "letter", b]:
                pa = scramble.index(a)
                pb = scramble.index(b)
                scramble[pa], scramble[pb] = scramble[pb], scramble[pa]
            case ["rotate", "left", a, _]:
                a = int(a)
                q = deque(scramble)
                q.rotate(-a)
                scramble = list(q)
            case ["rotate", "right", a, _]:
                a = int(a)
                q = deque(scramble)
                q.rotate(a)
                scramble = list(q)
            case ["rotate", "based", "on", "position", "of", "letter", a]:
                pa = scramble.index(a)
                if pa >= 4:
                    pa += 1
                pa += 1
                q = deque(scramble)
                q.rotate(pa)
                scramble = list(q)
            case ["reverse", "positions", a, "through", b]:
                a, b = int(a), int(b)
                scramble = scramble[:a] + scramble[a : b + 1][::-1] + scramble[b + 1 :]
            case ["move", "position", a, "to", "position", b]:
                a, b = int(a), int(b)
                c = scramble.pop(a)
                scramble.insert(b, c)

    return "".join(scramble)


def part1(data):
    word = "abcdefgh"
    return scramble(data, word)


def part2(data):
    word = "fbgdceah"
    for w in permutations(word):
        pword = "".join(w)
        if scramble(data, pword) == word:
            return pword


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
