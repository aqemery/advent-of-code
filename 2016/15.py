import sys


def solve(disks):
    disks.sort(reverse=True)
    time = 0
    while True:
        for num_pos, offset in disks:
            if (time + offset) % num_pos != 0:
                break
        else:
            return time
        time += 1


if __name__ == "__main__":
    data = sys.stdin.read().split("\n")

    disks = []
    for offset, l in enumerate(data):
        l = l.strip(".")
        _, _, _, num_pos, _, _, _, _, _, _, _, start_pos = l.split()
        num_pos = int(num_pos)
        start_pos = int(start_pos)
        disks.append((num_pos, (start_pos + offset + 1) % num_pos))
    print("part 1:", solve(disks))

    disks.append((11, len(disks) + 1))
    print("part 2:", solve(disks))
