import sys

ops = [l.split() for l in sys.stdin.readlines()]
visited = set()
pointer = 0
accumulator = 0

while not pointer in visited:
    visited.add(pointer)
    op = ops[pointer]
    f = op[0]

    if f == "jmp":
        pointer += int(op[1])
    elif f == "acc":
        accumulator += int(op[1])
        pointer += 1
    else:
        pointer += 1

print(accumulator)
