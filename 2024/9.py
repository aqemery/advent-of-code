from collections import deque

data = input()
disk = deque()
for i, c in enumerate(data):
    if i % 2 == 0:
        disk += [i // 2] * int(c)
    else:
        disk += [None] * int(c)

new_disk = []

while disk:
    item = disk.popleft()
    if item is not None:
        new_disk.append(item)
    else:
        while True and disk:
            if tail := disk.pop():
                new_disk.append(tail)
                break

p1 = sum(i * v for i, v in enumerate(new_disk))
print("part 1:", p1)


disk = deque()
for i, c in enumerate(data):
    if int(c) == 0:
        continue
    if i % 2 == 0:
        disk.append((int(c), i // 2))
    else:
        disk.append((int(c), None))


end = deque()

while disk:
    vlength, vid = disk.pop()
    if vid is None:
        end.insert(0, (vlength, None))
        continue

    next_disk = deque()
    while disk:
        length, id = disk.popleft()
        if id is not None:
            next_disk.append((length, id))
        elif vlength == length:
            next_disk.append((vlength, vid))
            end.insert(0, (vlength, None))
            break
        elif vlength < length:
            next_disk.append((vlength, vid))
            next_disk.append((length - vlength, None))
            end.insert(0, (vlength, None))
            break
        else:
            next_disk.append((length, None))
    else:
        end.insert(0, (vlength, vid))
    next_disk.extend(disk)
    disk = next_disk

out = []
while end:
    length, id = end.popleft()
    out += [id] * length

p2 = sum(i * v for i, v in enumerate(out) if v is not None)
print("part 2:", p2)
