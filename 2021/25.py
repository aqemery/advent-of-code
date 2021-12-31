import sys
import copy


def solve(sea):
    step = 0
    moved = True
    while step := step + 1:
        next = copy.deepcopy(sea)
        horz = step % 2
        exit = not moved
        moved = False
        for i, s in enumerate(sea):
            for j, c in enumerate(s):
                if horz and c == ">" and s[j - 1] == ".":
                    next[i][j] = "."
                    next[i][j - 1] = ">"
                    moved = True
                elif not horz and c == "v" and sea[i - 1][j] == ".":
                    next[i][j] = "."
                    next[i - 1][j] = "v"
                    moved = True

        if exit and not moved:
            break
        sea = next
    return step // 2 + 1


if __name__ == "__main__":
    sea = [list(reversed(l)) for l in reversed(sys.stdin.read().split("\n"))]
    print(solve(sea))
