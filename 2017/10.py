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


def part1(data):
    steps = [int(d) for d in data.split(",")]
    knot = list(range(knot_length))
    knot, _, _ = run_round(knot, steps)
    return knot[0] * knot[1]


def part2(data):
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
    d = input()
    print("part 1:", part1(d))
    print("part 2:", part2(d))
