
steps = 370

def part1():
    buffer = [0]
    i = 0
    for _ in range(2017):
        lb = len(buffer)
        i = (i + steps) % lb
        buffer = buffer[: i + 1] + [lb] + buffer[i + 1 :]
        i = (i + 1) % lb

    return buffer[i + 1]


def part2():
    i = 0
    out = None
    for v in range(1, 50000000):
        i = (i + steps) % v + 1
        if i == 1:
            out = v
    return out


if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())
