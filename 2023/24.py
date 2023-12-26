import sys
from itertools import combinations, count
from collections import defaultdict


def line(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (y1 - y2), (x2 - x1), -(x1 * y2 - x2 * y1)


def intersection(line1, line2):
    dy1, dx1, dxy1 = line(line1[0], line1[1])
    dy2, dx2, dxy2 = line(line2[0], line2[1])
    d = dy1 * dx2 - dx1 * dy2
    dx = dxy1 * dx2 - dx1 * dxy2
    dy = dy1 * dxy2 - dxy1 * dy2
    if d != 0:
        return dx / d, dy / d
    return False


def ray_check(pos, vol, intersect):
    if vol > 0 and intersect < pos:
        return False
    elif vol < 0 and intersect > pos:
        return False
    return True


def part1(data):
    min_v = 200000000000000
    max_v = 400000000000000

    total = 0
    for a, b in combinations(data, 2):
        ax, ay, _, avx, avy, _ = a
        bx, by, _, bvx, bvy, _ = b

        a = ((ax, ay), (ax + avx, ay + avy))
        b = ((bx, by), (bx + bvx, by + bvy))
        if intersect := intersection(a, b):
            xint, yint = intersect
            for pos, vol, inter in [
                (ax, avx, xint),
                (bx, bvx, xint),
                (ay, avy, yint),
                (by, bvy, yint),
            ]:
                if not ray_check(pos, vol, inter):
                    break
            else:
                if (min_v < xint < max_v) and (min_v < yint < max_v):
                    total += 1
    return total


def part2(data):
    positions = defaultdict(list)
    print(len(data))
    exit()
    for times in count():
        for i, (x, y, z, vx, vy, vz) in enumerate(data):
            positions[times].append((x, y, z, i))
            print(x, y, z)
    
        data = [(x+vx, y+vy, z+vz, vx, vy, vz) for x, y, z, vx, vy, vz in data]
        if times < 1000:
            continue 
        break

    print(positions)
        # if not some:
        #     break

        

        
            # print(x, y, z, vx, vy, vz)

        # x_step = data[0][0] + data[1][0]
        # # print(x_step)

        # for i in range(1, len(data)):
        #     if data[i][0] + data[i-1][0] != x_step:
        #         break
        # else:
        #     print("maybe", data)
        # # break
    
    




    return


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    d = [[int(x) for s in l.split("@") for x in s.split(",")] for l in d]

    print("part 1:", part1(d))
    print("part 2:", part2(d))
