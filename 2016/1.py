data = input().replace(",", "").split()
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
location_x = 0
location_y = 0
direction = 0

visited = set()
bunny_hq = None

for d in data:
    turn, *num_chars = d
    move_times = int("".join(num_chars))
    if turn == "L":
        direction -= 1
    else:
        direction += 1
    direction %= 4
    dir_x, dir_y = directions[direction]

    for _ in range(move_times):
        location_x += dir_x
        location_y += dir_y
        if (location_x, location_y) in visited and not bunny_hq:
            bunny_hq = abs(location_x) + abs(location_y)
        visited.add((location_x, location_y))

blocks_away = abs(location_x) + abs(location_y)

print("part 1:", blocks_away)
print("part 2:", bunny_hq)
