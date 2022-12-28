import sys
from dataclasses import dataclass


@dataclass
class Blizzard:
    pos: tuple
    step: tuple
    max_x: int
    max_y: int

    def move(self):
        x, y = self.pos
        dx, dy = self.step
        nx, ny = x + dx, y + dy

        if nx < 1:
            nx = self.max_x
        elif nx > self.max_x:
            nx = 1
        if ny < 1:
            ny = self.max_y
        elif ny > self.max_y:
            ny = 1

        self.pos = (nx, ny)


def walk(a, b, floor, weather):
    steps = set([a])

    count = 0
    while True:
        count += 1
        c_weather = set()
        for w in weather:
            w.move()
            c_weather.add(w.pos)

        next_steps = set()

        for s in steps:
            x, y = s

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]:
                n_pos = x + dx, y + dy
                if n_pos in floor and n_pos not in c_weather:
                    next_steps.add(n_pos)
                if n_pos == b:
                    return count
        steps = next_steps


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")

    max_x = len(d[0]) - 2
    max_y = len(d) - 2

    floor = set()
    weather = []
    for y, l in enumerate(d):
        for x, c in enumerate(l):
            direction = None
            if c == ">":
                direction = (1, 0)
            elif c == "<":
                direction = (-1, 0)
            elif c == "^":
                direction = (0, -1)
            elif c == "v":
                direction = (0, 1)
            if direction:
                weather.append(Blizzard((x, y), direction, max_x, max_y))

            if c in [">", "<", "^", "v", "."]:
                floor.add((x, y))

    start = min(floor, key=lambda x: x[1])
    end = max(floor, key=lambda x: x[1])

    p1 = walk(start, end, floor, weather)
    print("part 1:", p1)
    p2 = p1 + walk(end, start, floor, weather) + walk(start, end, floor, weather)
    print("part 2:", p2)
