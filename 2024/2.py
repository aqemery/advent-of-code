import sys

data = sys.stdin.read().split("\n")
lines = [[int(x) for x in l.split(" ")] for l in data]
invalids = []


def is_valid(l, first=True):
    if l[-1] < l[0]:
        l.reverse()
    for i in range(1, len(l)):
        delta = l[i] - l[i - 1]
        if delta > 3 or delta < 1:
            if first:
                invalids.append(l)
            return False
    return True


def remove_one_valid(l):
    for i in range(len(l)):
        current = l.copy()
        current.pop(i)
        if is_valid(current, False):
            return True
    return False


p1 = sum(is_valid(l) for l in lines)
print("part 1:", p1)

p2 = p1 + sum(remove_one_valid(l) for l in invalids)
print("part 2:", p2)
