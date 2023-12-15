def hash(value):
    hashval = 0
    for c in value:
        hashval = (hashval + ord(c)) * 17 % 256
    return hashval


def part1(data):
    return sum(hash(d) for d in data)


def part2(data):
    boxes = [[] for _ in range(256)]
    for op in data:
        if "-" == op[-1]:
            label = op[:-1]
            box_id = hash(label)
            boxes[box_id] = [l for l in boxes[box_id] if l[0] != label]
        else:
            label, lense = op.split("=")
            box = boxes[hash(label)]
            new_len = (label, int(lense))
            for i, (l, _) in enumerate(box):
                if l == label:
                    box[i] = new_len
                    break
            else:
                box.append(new_len)

    return sum(
        l[1] * (i + 1) * (j + 1)
        for i, box in enumerate(boxes)
        for j, l in enumerate(box)
    )


if __name__ == "__main__":
    d = input().split(",")
    print("part 1:", part1(d))
    print("part 2:", part2(d))
