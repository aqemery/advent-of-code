from math import sqrt

input_value = 34000000


def divisors(n):
    out = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            out.add(i)
            out.add(n // i)
    return out


def part1():
    h = 1
    while sum(divisors(h)) * 10 < input_value:
        h += 1
    return h


def part2():
    h = 1
    while sum(d for d in divisors(h) if d * 50 >= h) * 11 < input_value:
        h += 1
    return h


if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())
