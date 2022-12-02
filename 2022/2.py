import sys

dlw = [3, 0, 6]
f = ord('A')
s = ord('X')

def part1(data):
    score = 0 
    for a,b in data:
        fv = a-f
        sv = b-s
        score += dlw[fv-sv] + sv + 1
    return score


def part2(data):
    score = 0 
    for a,b in data:
        fv = a-f
        sv = b-s
        score += sv * 3 + (fv+sv-1) % 3 + 1 

    return score


if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    d = [[ord(c) for c in d.split()] for d in d]
    print("part 1:", part1(d))
    print("part 2:", part2(d))
