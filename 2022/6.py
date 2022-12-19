import sys


def solve(data, times):
    for i in range(times, len(d) + 1):
        if len(set(d[i - times : i])) == times:
            return i


if __name__ == "__main__":
    d = sys.stdin.read()
    print("part 1:", solve(d, 4))
    print("part 2:", solve(d, 14))
