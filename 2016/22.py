import sys


if __name__ == "__main__":
    data = sys.stdin.read().split("\n")
    max_x = 0
    max_y = 0
    nodes = {}
    for line in data:
        line = line.replace("T", "")
        node, size, used, availible, _ = line.split()
        node = node.replace("/dev/grid/node-x", "").replace("y", "")

        x, y = [int(a) for a in node.split("-")]
        max_x = max(max_x, x)
        max_y = max(max_y, y)

        nodes[(x, y)] = (int(size), int(used), int(availible))

    viable = 0
    for a in nodes.values():
        for b in nodes.values():
            if a == b or a[1] == 0:
                continue

            if a[1] <= b[2]:
                viable += 1
                print(a, b)

    print("part 1:", viable)

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if nodes[(x, y)][1] == 0:
                print("%", end="")
            elif nodes[(x, y)][1] >= 89:
                print("#", end="")
            else:
                print(".", end="")
        print()

    # 94 + 5 * 34 + 1
