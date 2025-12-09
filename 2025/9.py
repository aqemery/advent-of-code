import sys
from itertools import combinations
from shapely.geometry import Polygon, box


def part1(data):
    largest_area = 0
    for (a, b), (x, y) in combinations(data, 2):
        length = abs(a - x) + 1
        height = abs(b - y) + 1
        area = length * height
        if area > largest_area:
            largest_area = area
    return largest_area


def part2(data):
    largest_area = 0
    poly = Polygon(data)
    for (a, b), (x, y) in combinations(data, 2):
        length = abs(a - x) + 1
        height = abs(b - y) + 1
        area = length * height
        box_poly = box(min(a, x), min(b, y), max(a, x), max(b, y))
        if poly.contains(box_poly) and area > largest_area:
            largest_area = area
    return largest_area


if __name__ == "__main__":
    d = [[int(v) for v in line.split(",")] for line in sys.stdin.read().split("\n")]
    print("part 1:", part1(d))
    print("part 2:", part2(d))
