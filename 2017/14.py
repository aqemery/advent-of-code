from collections import deque
from itertools import batched

knot_length = 256


def reverse(knot, start, length):
    reverse = []
    for i in range(length):
        reverse.append(knot[(start + i) % knot_length])
    return reverse[::-1]


def run_round(knot, steps, i=0, skip=0):
    for s in steps:
        r = reverse(knot, i, s)
        for j in range(s):
            knot[i] = r[j]
            i = (i + 1) % knot_length
        i = (i + skip) % knot_length
        skip += 1
    return knot, i, skip


def make_knot(data):
    steps = [ord(c) for c in data]
    steps += [17, 31, 73, 47, 23]
    knot = list(range(knot_length))
    i = 0
    skip = 0

    for _ in range(64):
        knot, i, skip = run_round(knot, steps, i, skip)

    sparse = []
    for b in batched(knot, 16):
        v = b[0]
        for n in b[1:]:
            v ^= n
        sparse.append(v)
    return "".join(f"{hex(n)[2:]:0>2}" for n in sparse)


if __name__ == "__main__":
    grid = set()
    for i in range(128):
        d = f"jxqlasbh-{i}"
        knot = make_knot(d)
        row = ""
        for c in knot:
            hex_integer = int(c, 16)
            binary_string = bin(hex_integer)
            row += f"{binary_string[2:]:0>4}"
        for j, c in enumerate(row):
            if c == "1":
                grid.add((j, i))

    print("part 1:", len(grid))

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    groups = 0
    visted = set()
    for n in grid:
        if n not in visted:
            groups += 1
            q = deque([n])
            while q:
                node = q.popleft()
                if node not in grid or node in visted:
                    continue
                visted.add(node)
                x, y = node
                for dx, dy in dirs:
                    q.append((x + dx, y + dy))

                if (x, y) not in grid:
                    continue
    print("part 2:", groups)
