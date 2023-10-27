def redistribute(data):
    max_value = max(data)
    max_index = data.index(max_value)
    data[max_index] = 0
    dlen = len(data)
    current_index = (max_index + 1) % dlen

    for _ in range(max_value):
        data[current_index] += 1
        current_index = (current_index + 1) % dlen


def solve(data):
    data = [int(d) for d in data.split()]
    visited = {}
    visited[tuple(data)] = 0

    while True:
        redistribute(data)
        if tuple(data) in visited:
            return len(visited), len(visited) - visited[tuple(data)]
        visited[tuple(data)] = len(visited)


if __name__ == "__main__":
    d = input()
    p1, p2 = solve(d)
    print("part 1:", p1)
    print("part 2:", p2)
