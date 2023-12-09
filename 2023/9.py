import sys


def solve(data, reverse=1):
    all_numbers = []
    for line in data:
        numbers = [[int(n) for n in line.split()][::reverse]]
        while any(numbers[-1]):
            numbers.append([b-a for a, b in zip(numbers[-1], numbers[-1][1:])])
        all_numbers += numbers
    return sum(n[-1] for n in all_numbers)


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", solve(d))
    print("part 2:", solve(d, reverse=-1))