import sys


def part1(data):
    nice = 0
    for s in data:
        if any([g in s for g in ["ab", "cd", "pq", "xy"]]):
            continue
        vowels = 0
        doubles = 0
        last = None
        for c in s:
            if c in "aeiou":
                vowels += 1
            if c == last:
                doubles += 1
            last = c

        if vowels >= 3 and doubles:
            nice += 1
    return nice


def part2(data):
    nice = 0
    for s in data:
        alternate = False
        for i, c in enumerate(s[:-2]):
            if c == s[i + 2]:
                alternate = True
                break

        last = None
        pair = False
        for i, c in enumerate(s):
            if f"{last}{c}" in s[i + 1 :]:
                pair = True
                break
            last = c

        if alternate and pair:
            nice += 1
    return nice


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
