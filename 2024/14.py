import sys
import math

width, height = 101, 103
raw_in = sys.stdin.read()
raw_in = raw_in.replace("p=", "")
raw_in = raw_in.replace(" v=", ",")
robots = [l.split(",") for l in raw_in.splitlines()]
robots = [[int(v) for v in r] for r in robots]

for i in range(1000000):
    for r in robots:
        r[0] += r[2]
        r[1] += r[3]
        if r[0] < 0:
            r[0] += width
        if r[0] >= width:
            r[0] -= width
        if r[1] < 0:
            r[1] += height
        if r[1] >= height:
            r[1] -= height

    if i == 100:
        quad = [0, 0, 0, 0]
        for r in robots:
            if r[0] < width / 2 - 1:
                if r[1] < height / 2 - 1:
                    quad[0] += 1
                elif r[1] > height / 2:
                    quad[1] += 1
            elif r[0] > width / 2:
                if r[1] < height / 2 - 1:
                    quad[2] += 1
                elif r[1] > height / 2:
                    quad[3] += 1

        print("p1:", math.prod(quad))

    robots_set = set((r[0], r[1]) for r in robots)
    if len(robots_set) != len(robots):
        continue


    print('p2:', i+1)
    break
    # for y in range(height):
    #     for x in range(width):
    #         for r in robots:
    #             if r[0] == x and r[1] == y:
    #                 print('x', end="")
    #                 break
    #         else:
    #             print(' ', end="")
    #     print()
    # break




