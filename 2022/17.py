from collections import deque


line_rock = [(x + 2, 0 + 3) for x in range(4)]
plus_rock = [(x + 2, y + 3) for x in range(3) for y in range(3) if x == 1 or y == 1]
l_rock = [(x + 2, y + 3) for x in range(3) for y in range(3) if x == 2 or y == 0]
line_down_rock = [(2, y + 3) for y in range(4)]
square_rock = [(x + 2, y + 3) for x in range(2) for y in range(2)]


def solve(data, times):
    jets = jetGen(data)
    rocks = rockGen()
    tower = set()
    height = 0
    first_floor = None
    extra_height = 0

    num_dropped = 0

    while num_dropped < times:
        r = next(rocks)
        r = [(x, y + height) for x, y in r]
        num_dropped += 1
        check_repeat = True

        if check_repeat and all((x, height -1) in tower for x in range(7)):
            if first_floor is None:
                first_floor = (height, num_dropped)
            else:
                check_repeat = False
                rocks_droped = num_dropped - first_floor[1]
                repeat_height = height - first_floor[0]
                repeat_times = (times - first_floor[1]) // rocks_droped
                num_dropped -= rocks_droped
                num_dropped += repeat_times * rocks_droped
                extra_height += (repeat_times - 1) * repeat_height
                rocks_droped = times - (times - first_floor[1]) % rocks_droped

        nh = dropRock(r, tower, jets)
        if nh > height:
            height = nh
    if extra_height:
        height += extra_height

    return height


def dropRock(r, tower, jets):
    while True:
        j = next(jets)
        nr = []
        for x, y in r:
            nx = x + j
            if nx < 0 or nx > 6 or (nx, y) in tower:
                break
            nr.append((nx, y))
        else:
            r = nr
        
        nr = []
        for x, y in r:
            ny = y - 1
            if ny < 0 or (x, ny) in tower:
                tower.update(r)
                return max([ry for _, ry in r]) + 1
            nr.append((x, ny))
        else:
            r = nr
        

def shiftRock(rock, j):
    nr = []
    for x, y in rock:
        nx = x + j
        if nx < 0 or nx > 6:
            return rock
        nr.append((nx, y))
    return nr


def part2(data):
    return


def rockGen():
    q = deque([line_rock, plus_rock, l_rock, line_down_rock, square_rock])
    while q:
        yield q[0]
        q.rotate(-1)


def jetGen(data):
    q = deque([(1, -1)[d == '<'] for d in data])
    while q:
        yield q[0]
        q.rotate(-1)


if __name__ == "__main__":
    d = input()
    print("part 1:", solve(d, 2022))
    print("part 2:", solve(d, 1_000_000_000_000))
