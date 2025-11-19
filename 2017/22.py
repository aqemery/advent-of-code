def parse(filename):
    with open(filename) as f:
        grid = [line.strip() for line in f]

    infected = set()
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == '#':
                infected.add((x, y))

    # Start position is center of grid
    start_x = len(grid[0]) // 2
    start_y = len(grid) // 2

    return infected, (start_x, start_y)


def part1(infected, start):
    infected = set(infected)  # Copy
    x, y = start
    dx, dy = 0, -1  # Facing up

    infections = 0

    for _ in range(10000):
        if (x, y) in infected:
            # Turn right
            dx, dy = -dy, dx
            infected.remove((x, y))
        else:
            # Turn left
            dx, dy = dy, -dx
            infected.add((x, y))
            infections += 1

        # Move forward
        x += dx
        y += dy

    return infections


def part2(infected_set, start):
    # States: 0=clean, 1=weakened, 2=infected, 3=flagged
    states = {}
    for pos in infected_set:
        states[pos] = 2  # infected

    x, y = start
    dx, dy = 0, -1  # Facing up

    infections = 0

    for _ in range(10000000):
        state = states.get((x, y), 0)

        if state == 0:  # Clean
            # Turn left
            dx, dy = dy, -dx
            states[(x, y)] = 1  # Weakened
        elif state == 1:  # Weakened
            # No turn
            states[(x, y)] = 2  # Infected
            infections += 1
        elif state == 2:  # Infected
            # Turn right
            dx, dy = -dy, dx
            states[(x, y)] = 3  # Flagged
        else:  # Flagged
            # Reverse
            dx, dy = -dx, -dy
            del states[(x, y)]  # Clean

        # Move forward
        x += dx
        y += dy

    return infections


if __name__ == '__main__':
    infected, start = parse('2017/input')

    print(f"Part 1: {part1(infected, start)}")
    print(f"Part 2: {part2(infected, start)}")
