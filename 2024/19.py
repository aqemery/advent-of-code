from functools import cache

def parse(filename):
    with open(filename) as f:
        parts = f.read().strip().split('\n\n')
    patterns = tuple(p.strip() for p in parts[0].split(','))
    designs = parts[1].split('\n')
    return patterns, designs

def solve(patterns, designs):
    @cache
    def count_ways(design):
        if not design:
            return 1
        total = 0
        for p in patterns:
            if design.startswith(p):
                total += count_ways(design[len(p):])
        return total

    ways = [count_ways(d) for d in designs]
    return sum(1 for w in ways if w > 0), sum(ways)

if __name__ == '__main__':
    patterns, designs = parse('/Users/adamemery/advent-of-code/2024/input19')
    p1, p2 = solve(patterns, designs)
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
