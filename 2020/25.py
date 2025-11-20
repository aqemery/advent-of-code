def parse(filename):
    with open(filename) as f:
        lines = f.read().strip().split('\n')
    return int(lines[0]), int(lines[1])

def find_loop_size(public_key):
    value = 1
    subject = 7
    loop_size = 0
    while value != public_key:
        value = (value * subject) % 20201227
        loop_size += 1
    return loop_size

def transform(subject, loop_size):
    value = 1
    for _ in range(loop_size):
        value = (value * subject) % 20201227
    return value

def part1(card_public, door_public):
    card_loop = find_loop_size(card_public)
    encryption_key = transform(door_public, card_loop)
    return encryption_key

if __name__ == '__main__':
    card_public, door_public = parse('/Users/adamemery/advent-of-code/2020/input25')
    print(f"Part 1: {part1(card_public, door_public)}")
    print(f"Part 2: (free star)")
