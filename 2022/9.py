import sys
import math
from dataclasses import dataclass


dirs = {"R": (1, 0), "U": (0, 1), "L": (-1, 0), "D": (0, -1)}


@dataclass
class Knot:
    x: int = 0
    y: int = 0

    def follow(self, r):
        hx, hy = r.pos()
        mx = abs(self.x - hx)
        my = abs(self.y - hy)
        mult = 1
        if my == 2 and mx == 2:
            mult = 2
        if my == 2 and mx == 1:
            self.x = hx
        if my == 1 and mx == 2:
            self.y = hy

        dist = abs(self.x - hx) + abs(self.y - hy)

        if dist > 1:
            angle = math.atan2(self.x - hx, self.y - hy)
            move_by_cos = -math.cos(angle) * mult
            move_by_sin = -math.sin(angle) * mult
            self.move(int(move_by_sin), int(move_by_cos))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def pos(self):
        return (self.x, self.y)


def solve(data, times):
    locations = set()
    rope = [Knot() for _ in range(times)]
    for d in data:
        dirt, t = d.split()
        for _ in range(int(t)):
            rope[0].move(*dirs[dirt])
            for i, r in enumerate(rope[1:]):
                r.follow(rope[i])
            locations.add(rope[-1].pos())

    return len(locations)


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", solve(d, 2))
    print("part 2:", solve(d, 10))
