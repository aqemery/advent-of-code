import sys
from collections import deque

def parseStacks(lines):
    stacks = [deque() for _ in range(len(lines) + 1)]

    for l in lines:
        for i, v in enumerate(l):
            if v != " ":
                stacks[i].append(v)

    return stacks


def part1(lines, data):
    stacks = parseStacks(lines)
    for d in data:
        c, f, t = [int(i)-1 for i in d.split()[1::2]]
        for _ in range(int(c)+1):
            stacks[t].append(stacks[f].pop())
    
    return ''.join([s.pop() for s in stacks])


def part2(lines, data):
    stacks = parseStacks(lines)
    for d in data:
        c, f, t = [int(i)-1 for i in d.split()[1::2]]
        temp = deque()
        for _ in range(int(c)+1):
            temp.append(stacks[f].pop())
        for _ in range(len(temp)):
            stacks[t].append(temp.pop())

    
    return ''.join([s.pop() for s in stacks])


if __name__ == "__main__":
    s_in, data = sys.stdin.read().split("\n\n")
    data = data.split('\n')
    lines = [[s[i] for i in range(1,len(s),4)] for s in s_in.split('\n')[:-1]]
    lines.reverse()
    print("part 1:", part1(lines, data))
    print("part 2:", part2(lines, data))
