import re

def part1(data):
    out = ""
    while next_marker := re.search(r"\(\d+x\d+\)", data):
        start, end = next_marker.span()
        next_marker = next_marker.group()[1:-1]
        num_chars, times = [int(x) for x in next_marker.split("x")]
        out += data[:start]
        data = data[end:]

        next_select = data[:num_chars]
        out += next_select * times
        data = data[num_chars:]

    if data:
        out += data
    return len(out)


def part2(data):
    mutiplyer = [1 for c in data]
    marker_lengths = 0

    for marker in re.finditer(r"\(\d+x\d+\)", data):
        marker_data = marker.group()[1:-1]
        num_chars, times = [int(x) for x in marker_data.split("x")]
        marker_lengths += len(marker.group())

        for i in range(len(marker_data) + 2):
            mutiplyer[marker.start() + i] = 1

        for i in range(num_chars):
            mutiplyer[marker.end() + i] *= times

    return sum(mutiplyer) - marker_lengths


if __name__ == "__main__":
    d = input()
    print("part 1:", part1(d))
    print("part 2:", part2(d))
