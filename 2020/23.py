def parse(filename):
    with open(filename) as f:
        return [int(c) for c in f.read().strip()]

def play(cups, moves):
    n = len(cups)
    # Build linked list: next[i] = cup after cup i
    next_cup = [0] * (n + 1)
    for i in range(len(cups)):
        next_cup[cups[i]] = cups[(i + 1) % len(cups)]

    current = cups[0]

    for _ in range(moves):
        # Pick up 3 cups
        p1 = next_cup[current]
        p2 = next_cup[p1]
        p3 = next_cup[p2]
        picked = {p1, p2, p3}

        # Find destination
        dest = current - 1
        if dest == 0:
            dest = n
        while dest in picked:
            dest -= 1
            if dest == 0:
                dest = n

        # Remove picked cups
        next_cup[current] = next_cup[p3]

        # Insert after destination
        next_cup[p3] = next_cup[dest]
        next_cup[dest] = p1

        # Move to next
        current = next_cup[current]

    return next_cup

def part1(cups):
    next_cup = play(cups, 100)

    result = []
    current = next_cup[1]
    while current != 1:
        result.append(str(current))
        current = next_cup[current]

    return ''.join(result)

def part2(cups):
    # Extend to 1 million cups
    cups = cups + list(range(len(cups) + 1, 1000001))
    next_cup = play(cups, 10000000)

    c1 = next_cup[1]
    c2 = next_cup[c1]
    return c1 * c2

if __name__ == '__main__':
    cups = parse('/Users/adamemery/advent-of-code/2020/input23')
    print(f"Part 1: {part1(cups)}")
    print(f"Part 2: {part2(cups)}")
