import sys


def mirror(lines):
    for mir in range(1, len(lines)):
        errors = 0
        for before, after in zip(lines[:mir][::-1], lines[mir:]):
            errors += sum(a != b for a, b in zip(before, after))
        if errors == smudge:
            return mir


def process_group(lines):
    if vm := mirror(lines):
        return vm * 100
    if hm := mirror(["".join(l) for l in zip(*lines)]):
        return hm


def solve(data):
    return sum(process_group(g) for g in data)


if __name__ == "__main__":
    d = [g.split("\n") for g in sys.stdin.read().split("\n\n")]
    smudge = 0
    print("part 1:", solve(d))
    smudge = 1
    print("part 2:", solve(d))
