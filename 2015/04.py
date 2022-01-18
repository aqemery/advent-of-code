import hashlib


def solve(data, times):
    a = 0

    while r := hashlib.md5(f"{data}{a}".encode()):
        if r.hexdigest().startswith("0" * times):
            return a
        a += 1


if __name__ == "__main__":
    d = input()
    print("part 1:", solve(d, 5))
    print("part 2:", solve(d, 6))
