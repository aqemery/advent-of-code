import re
import sys
sys.setrecursionlimit(100000)

def parse_input(filename):
    clay = set()
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith('x='):
                match = re.match(r'x=(\d+), y=(\d+)\.\.(\d+)', line)
                x = int(match.group(1))
                y1, y2 = int(match.group(2)), int(match.group(3))
                for y in range(y1, y2 + 1):
                    clay.add((x, y))
            else:
                match = re.match(r'y=(\d+), x=(\d+)\.\.(\d+)', line)
                y = int(match.group(1))
                x1, x2 = int(match.group(2)), int(match.group(3))
                for x in range(x1, x2 + 1):
                    clay.add((x, y))
    return clay

def simulate_water(clay):
    min_y = min(y for x, y in clay)
    max_y = max(y for x, y in clay)

    flowing = set()
    settled = set()

    def fill(x, y):
        # Mark as flowing
        flowing.add((x, y))

        # Flow down if possible
        if (x, y + 1) not in clay and (x, y + 1) not in flowing and y + 1 <= max_y:
            fill(x, y + 1)

        # If below is not blocked, we can't spread
        if (x, y + 1) not in clay and (x, y + 1) not in settled:
            return

        # Spread left
        left_blocked = False
        lx = x - 1
        while (lx, y) not in clay:
            flowing.add((lx, y))
            if (lx, y + 1) not in clay and (lx, y + 1) not in settled:
                # Can fall here
                fill(lx, y)
                break
            lx -= 1
        else:
            left_blocked = True

        # Spread right
        right_blocked = False
        rx = x + 1
        while (rx, y) not in clay:
            flowing.add((rx, y))
            if (rx, y + 1) not in clay and (rx, y + 1) not in settled:
                # Can fall here
                fill(rx, y)
                break
            rx += 1
        else:
            right_blocked = True

        # If both sides are blocked by walls, settle this row
        if left_blocked and right_blocked:
            for sx in range(lx + 1, rx):
                settled.add((sx, y))
                flowing.discard((sx, y))

    fill(500, min_y)

    water_reach = len([p for p in flowing | settled if min_y <= p[1] <= max_y])
    settled_count = len([p for p in settled if min_y <= p[1] <= max_y])

    return water_reach, settled_count

if __name__ == '__main__':
    clay = parse_input('/Users/adamemery/advent-of-code/2018/input17')
    part1, part2 = simulate_water(clay)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
