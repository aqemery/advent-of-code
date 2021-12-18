import sys

empty = set()
filled = {
    (x, y)
    for y, l in enumerate(sys.stdin.readlines())
    for x, c in enumerate(l.strip())
    if c == "L"
}


def add(a, b):
    return tuple(sum(z) for z in zip(a, b))


around = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]
around.remove((0, 0))


def run():
    new_empty = set()
    new_filled = set()

    for t in empty:
        for a in around:
            check = add(t, a)
            if check in filled:
                new_empty.add(t)
                break
        else:
            new_filled.add(t)

    for t in filled:
        count = 0
        for a in around:
            check = add(t, a)
            if check in filled:
                count += 1
        if count >= 4:
            new_empty.add(t)
        else:
            new_filled.add(t)

    return new_empty, new_filled


last = empty
empty, filled = run()

while last != empty:
    last = empty
    empty, filled = run()

print(len(filled))
