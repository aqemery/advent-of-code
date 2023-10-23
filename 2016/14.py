from collections import defaultdict
import hashlib


def solve(part2=False):
    salt = "qzyelonm"
    found = []
    to_validate = defaultdict(list[int])

    i = 0
    stop = None
    while stop is None or i < stop:
        hash_code = f"{salt}{i}".encode()
        hex = hashlib.md5(hash_code).hexdigest()

        if part2:
            for _ in range(2016):
                hash_code = hex.encode()
                hex = hashlib.md5(hash_code).hexdigest()

        last = None
        triple_found = None

        for c in hex:
            if c == last:
                char_count += 1
            else:
                char_count = 1
            last = c

            if char_count == 3 and not triple_found:
                triple_found = c

            if char_count == 5:
                for j in to_validate[c]:
                    if i - j <= 1000:
                        found.append(j)
                    if len(found) == 64:
                        stop = i + 1000
                to_validate[c] = []

        if triple_found:
            to_validate[triple_found].append(i)

        i += 1
    return sorted(found)[63]


if __name__ == "__main__":
    print("part 1:", solve())
    print("part 2:", solve(part2=True))
