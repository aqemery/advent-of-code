import sys
from dataclasses import dataclass


@dataclass()
class Sub:
    depth: int = 0
    horizontal: int = 0
    aim: int = 0

    def move_depth(self, x):
        self.depth += x

    def move_horizontal(self, x):
        self.horizontal += x
        self.depth += x * self.aim
    
    def move_aim(self, x):
        self.aim += x


def part1(lines):
    sub = Sub()
    for l in lines:
        k, v = l.split()
        v = int(v)
        match k:
            case 'forward':
                sub.move_horizontal(v)
            case 'up':
                sub.move_depth(-v)
            case 'down':
                sub.move_depth(v)

    return sub.depth * sub.horizontal


def part2(lines):
    sub = Sub()
    for l in lines:
        k, v = l.split()
        v = int(v)
        match k:
            case 'forward':
                sub.move_horizontal(v)
            case 'up':
                sub.move_aim(-v)
            case 'down':
                sub.move_aim(v)

    return sub.depth * sub.horizontal


def main():
    lines = sys.stdin.readlines()
    print("part 1:", part1(lines))
    print("part 2:", part2(lines))


if __name__ == "__main__":
    main()
