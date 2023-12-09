import sys


def solve(data, index=-1, fun=lambda a, b: b - a):
    all_numbers = []
    for line in data:
        numbers = [[int(n) for n in line.split()]]
        while any(numbers[-1]):
            numbers.append([fun(a, b) for a, b in zip(numbers[-1], numbers[-1][1:])])
        all_numbers += numbers
    return sum(n[index] for n in all_numbers)


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", solve(d))
    print("part 2:", solve(d, index=0, fun=lambda a, b: a - b))
