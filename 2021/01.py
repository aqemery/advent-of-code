import sys


def part1(depths):
    return len([v for i, v in enumerate(depths) if v > depths[i - 1]])


def part2(depths):
    threesum = [sum(depths[i : i + 3]) for i in range(0, len(depths[:-2]))]
    return part1(threesum)


if __name__ == "__main__":
    depths = list(map(int, sys.stdin.readlines()))
    print("part 1:", part1(depths))
    print("part 2:", part2(depths))
