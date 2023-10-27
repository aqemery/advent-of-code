import sys
from collections import Counter
from functools import cache


@cache
def get_weight(node):
    size = 0
    if node in forward_tree:
        for n in forward_tree[node]:
            size += get_weight(n)
    return size + weights[node]


if __name__ == "__main__":
    data = sys.stdin.read().split("\n")
    tree = {}
    forward_tree = {}
    weights = {}

    for line in data:
        line = (
            line.replace(",", "").replace("(", "").replace(")", "").replace(" -> ", " ")
        )
        name, weight, *connections = line.split()
        weights[name] = int(weight)
        for c in connections:
            tree[c] = name
        forward_tree[name] = connections

    current = list(tree.keys())[0]
    while True:
        next = tree.get(current)
        if next is None:
            break
        current = next

    print("part 1:", current)

    current_sizes = None
    while True:
        current_items = forward_tree[current]
        previous_sizes = current_sizes
        current_sizes = [get_weight(n) for n in current_items]
        for i, cs in enumerate(current_sizes):
            if current_sizes.count(cs) == 1:
                current = current_items[i]
                break

        else:
            break

    target_size = Counter(previous_sizes).most_common()[0][0]
    size = target_size - sum(current_sizes)
    print("part 2:", size)
