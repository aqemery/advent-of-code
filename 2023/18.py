import sys
from shapely.geometry.polygon import Polygon


dirs = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, -1),
    "D": (0, 1),
}


def part1(data):
    path = [(0, 0)]
    cx, cy = 0, 0
    for line in data:
        direction, steps, _ = line.split()
        dx, dy = dirs[direction]
        cx += dx * int(steps)
        cy += dy * int(steps)
        path.append((cx, cy))
    poly = Polygon(path)
    return int((poly.length / 2) + poly.area + 1)


def part2(data):
    dir_nums = ["R", "D", "L", "U"]
    new_data = []
    for line in data:
        _, _, hex_val = line.split()
        hex_val = hex_val[2:-1]
        letter = dir_nums[int(hex_val[-1])]
        num = int(hex_val[:-1], 16)
        new_data.append(f"{letter} {num} garbage")
    return part1(new_data)


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
