import sys


def next_highest(search):
    for j in range(9, 0, -1):
        for i, v in enumerate(search):
            if v == str(j):
                return v, i + 1


def solve(data, size):
    total = 0
    for d in data:
        last_index = 0
        values = ""
        for i in range(size):
            max_index = -size + i + 1 or None
            search = d[last_index:max_index]
            v, lx = next_highest(search)
            last_index += lx
            values += str(v)
        total += int(values)
    return total


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", solve(d, 2))
    print("part 2:", solve(d, 12))
