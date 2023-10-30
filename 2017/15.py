from collections import deque 

factor_a = 16807
factor_b = 48271
divisor = 2147483647


def part1():
    generator_a = 679
    generator_b = 771
    total = 0
    for _ in range(40_000_000):
        generator_a = (generator_a * factor_a) % divisor
        generator_b = (generator_b * factor_b) % divisor
        if generator_a & 0xFFFF == generator_b & 0xFFFF:
            total += 1
    return total


def part2():
    generator_a = 679
    generator_b = 771
    total = 0
    judge_a = deque()
    judge_b = deque()

    for _ in range(40_000_000):
        generator_a = (generator_a * factor_a) % divisor
        generator_b = (generator_b * factor_b) % divisor
        if generator_a % 4 == 0:
            judge_a.append(generator_a)
        if generator_b % 8 == 0:
            judge_b.append(generator_b)

        if len(judge_a) > 0 and len(judge_b) > 0:
            if judge_a.popleft() & 0xFFFF == judge_b.popleft() & 0xFFFF:
                total += 1
    return total


if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())
