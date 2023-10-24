from itertools import batched


def dragon(a):
    b = a[::-1]
    b = [("1", "0")[c == "1"] for c in b]
    return f"{a}0{''.join(b)}"


def solve(disk_size=272):
    data = "10001001100000001"
    while len(data) < disk_size:
        data = dragon(data)

    data = data[:disk_size]
    checksum = data
    while len(checksum) % 2 == 0:
        checksum = "".join([("0", "1")[a == b] for a, b in batched(checksum, 2)])

    return checksum


if __name__ == "__main__":
    print("part 1:", solve())
    print("part 2:", solve(disk_size=35651584))
