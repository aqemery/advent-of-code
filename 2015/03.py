def move(c, santa):
    if c == ">":
        santa[0] += 1
    elif c == "<":
        santa[0] -= 1
    elif c == "^":
        santa[1] += 1
    else:
        santa[1] -= 1


def part1(data):
    cur = [0, 0]
    visited = set(cur)
    visited.add((0, 0))

    for c in data:
        move(c, cur)
        visited.add(tuple(cur))

    return len(visited)


def part2(data):
    cur = [0, 0]
    cur2 = [0, 0]
    visited = set()
    visited.add((0, 0))
    for c in data[::2]:
        move(c, cur)
        visited.add(tuple(cur))

    for c in data[1::2]:
        move(c, cur2)
        visited.add(tuple(cur2))

    return len(visited)


if __name__ == "__main__":
    i = input()
    print("part 1:", part1(i))
    print("part 2:", part2(i))
