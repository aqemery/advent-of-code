import sys


def solve(data, p2=False):
    jumps = [int(l) for l in data]
    i = 0
    steps = 0
    while True:
        steps += 1
        try:
            if jumps[i] >= 3 and p2:
                jumps[i] -= 1
                i += jumps[i] + 1
            else:
                jumps[i] += 1
                i += jumps[i] - 1

        except IndexError:
            return steps - 1


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", solve(d))
    print("part 2:", solve(d, True))
