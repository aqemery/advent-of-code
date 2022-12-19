import sys
from dataclasses import dataclass
from math import prod

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


@dataclass
class Tree:
    height: int
    visible: bool = False


def lineOfSight(forest, pos_x, pos_y, dir_x, dir_y):
    cur = -1
    try:
        while t := forest[(pos_x, pos_y)]:
            if t.height > cur:
                t.visible = True
                cur = t.height
            pos_x += dir_x
            pos_y += dir_y
    except KeyError:
        return


def seeTrees(tree, cx, cy):
    height = tree.height
    scores = []
    for dir_x, dir_y in dirs:
        score = 0
        pos_x = cx + dir_x
        pos_y = cy + dir_y
        try:
            while t := forest[(pos_x, pos_y)]:
                score += 1
                if t.height >= tree.height:
                    break
                pos_x += dir_x
                pos_y += dir_y
        except KeyError:
            pass
        scores.append(score)
    return prod(scores)


if __name__ == "__main__":
    forest = {}
    d = sys.stdin.read().split("\n")
    for y, l in enumerate(d):
        for x, v in enumerate(l):
            forest[(x, y)] = Tree(height=int(v))

    l = len(d)

    for i in range(l):
        lineOfSight(forest, 0, i, 1, 0)
        lineOfSight(forest, i, 0, 0, 1)
        lineOfSight(forest, l - 1, i, -1, 0)
        lineOfSight(forest, i, l - 1, 0, -1)

    p1 = sum(t.visible for t in forest.values())
    p2 = max(seeTrees(v, *k) for k, v in forest.items())

    print("part 1:", p1)
    print("part 2:", p2)
