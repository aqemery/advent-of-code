import sys


def check(pixels, values, value):
    values.append(value)
    if abs(len(pixels) % 40 - value) < 2:
        pixels.append("#")
    else:
        pixels.append(".")


if __name__ == "__main__":
    data = sys.stdin.read().split("\n")
    pixels = []
    values = []
    value = 1
    for d in data:
        check(pixels, values, value)
        if "noop" not in d:
            check(pixels, values, value)
            value += int(d.split()[-1])

    p1 = sum([v * (i + 1) for i, v in enumerate(values) if (i + 1 - 20) % 40 == 0])
    print("part 1:", p1)
    print("part 2:")

    for i, p in enumerate(pixels):
        if (i) % 40 == 0:
            print()
        print(p, end="")
