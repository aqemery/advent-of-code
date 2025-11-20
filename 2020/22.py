from collections import deque

def parse(filename):
    with open(filename) as f:
        parts = f.read().strip().split('\n\n')

    deck1 = deque(int(x) for x in parts[0].split('\n')[1:])
    deck2 = deque(int(x) for x in parts[1].split('\n')[1:])
    return deck1, deck2

def part1(deck1, deck2):
    d1, d2 = deque(deck1), deque(deck2)

    while d1 and d2:
        c1, c2 = d1.popleft(), d2.popleft()
        if c1 > c2:
            d1.extend([c1, c2])
        else:
            d2.extend([c2, c1])

    winner = d1 if d1 else d2
    return sum(card * (len(winner) - i) for i, card in enumerate(winner))

def recursive_combat(d1, d2):
    seen = set()

    while d1 and d2:
        state = (tuple(d1), tuple(d2))
        if state in seen:
            return 1, d1
        seen.add(state)

        c1, c2 = d1.popleft(), d2.popleft()

        if len(d1) >= c1 and len(d2) >= c2:
            winner, _ = recursive_combat(
                deque(list(d1)[:c1]),
                deque(list(d2)[:c2])
            )
        else:
            winner = 1 if c1 > c2 else 2

        if winner == 1:
            d1.extend([c1, c2])
        else:
            d2.extend([c2, c1])

    if d1:
        return 1, d1
    return 2, d2

def part2(deck1, deck2):
    _, winner_deck = recursive_combat(deque(deck1), deque(deck2))
    return sum(card * (len(winner_deck) - i) for i, card in enumerate(winner_deck))

if __name__ == '__main__':
    deck1, deck2 = parse('/Users/adamemery/advent-of-code/2020/input22')
    print(f"Part 1: {part1(deck1, deck2)}")
    print(f"Part 2: {part2(deck1, deck2)}")
