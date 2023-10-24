import sys


def next_row(row):
    next_row = []
    for i in range(len(row)):
        left = row[i - 1] if i > 0 else "."
        right = row[i + 1] if i < len(row) - 1 else "."
        if (left == "^") ^ (right == "^"):
            next_row.append("^")
        else:
            next_row.append(".")

    return "".join(next_row)


def solve(row, times):
    rows = [row]
    for _ in range(times - 1):
        rows.append(next_row(rows[-1]))
    return "".join(rows).count(".")


if __name__ == "__main__":
    d = input()

    print("part 1:", solve(d, 40))
    print("part 2:", solve(d, 400000))
