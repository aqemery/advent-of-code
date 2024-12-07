import sys
from collections import deque

lines = sys.stdin.read().splitlines()
lines = [l.split(": ") for l in lines]


def check(test, values, concat=False):
    values = [int(v) for v in values.split(" ")]
    test = int(test)
    q = deque([(values[0], values[1:])])
    while q:
        current, values = q.popleft()
        if not values:
            if current == test:
                return test
        elif not current > test:
            q.append((current * values[0], values[1:]))
            q.append((current + values[0], values[1:]))
            if concat:
                q.append((int(str(current) + str(values[0])), values[1:]))
    return False


print("p1:", sum(check(test, values) for test, values in lines))
print("p2:", sum(check(test, values, True) for test, values in lines))
