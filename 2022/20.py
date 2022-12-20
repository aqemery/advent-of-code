import sys


class Node:
    value = None
    left = None
    right = None

    def __init__(self, value):
        self.value = value


def solve(data, times=1):
    order = [Node(v) for v in data]
    head = None
    l = len(data) - 1

    for i, n in enumerate(order):
        n.left = order[i - 1]
        r = i + 1
        if r == len(data):
            r = 0
        n.right = order[r]
        if n.value == 0:
            head = n

    for _ in range(times):
        for n in order:
            next_node = n
            if n.value == 0:
                continue

            n.left.right = n.right
            n.right.left = n.left
            for _ in range(abs(n.value) % l):
                if n.value > 0:
                    next_node = next_node.right
                else:
                    next_node = next_node.left
            if n.value < 0:
                next_node = next_node.left

            next_node.right.left = n
            n.right = next_node.right
            n.left = next_node
            next_node.right = n

    values = []
    cur = head
    for _ in range(3):
        for _ in range(1000):
            cur = cur.right
        values.append(cur.value)
    return sum(values)


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    d = [int(x) for x in d]
    print("part 1:", solve(d))
    d = [x * 811589153 for x in d]
    print("part 2:", solve(d, 10))
