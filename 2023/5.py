import sys
from itertools import batched, count


def get_input(data):
    _, *seeds = data[0].split()
    seeds = [int(s) for s in seeds]
    transforms = []
    for group in data[1:]:
        group_transforms = []
        for line in group.split("\n")[1:]:
            group_transforms.append([int(c) for c in line.split()])
        transforms.append(group_transforms)
    return seeds, transforms


def part1(data):
    seeds, transforms = get_input(data)

    lowest = None
    for seed in seeds:
        for group in transforms:
            for dest, source, length in group:
                if source <= seed < source + length:
                    seed = dest + (seed - source)
                    break
        if lowest is None:
            lowest = seed
        elif seed < lowest:
            lowest = seed
    return lowest


def part2(data):
    seeds, transforms = get_input(data)
    transforms = transforms[::-1]

    for lowest in count():
        seed = lowest
        for group in transforms:
            for dest, source, length in group:
                if dest <= seed < dest + length:
                    seed = (seed - dest) + source
                    break

        if any(s <= seed < (s + r) for s, r in batched(seeds, 2)):
            return lowest


if __name__ == "__main__":
    d = sys.stdin.read().split("\n\n")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
    