def parse(filename):
    with open(filename) as f:
        blocks = f.read().strip().split('\n\n')

    locks = []
    keys = []

    for block in blocks:
        lines = block.split('\n')
        heights = []
        for col in range(len(lines[0])):
            count = sum(1 for row in lines if row[col] == '#') - 1
            heights.append(count)

        if lines[0][0] == '#':
            locks.append(heights)
        else:
            keys.append(heights)

    return locks, keys

def part1(locks, keys):
    count = 0
    for lock in locks:
        for key in keys:
            if all(l + k <= 5 for l, k in zip(lock, key)):
                count += 1
    return count

if __name__ == '__main__':
    locks, keys = parse('/Users/adamemery/advent-of-code/2024/input25')
    print(f"Part 1: {part1(locks, keys)}")
    print(f"Part 2: (free star)")
