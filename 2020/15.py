input_line = [2, 15, 0, 9, 1, 20]

visited = {v: (i + 1) for i, v in enumerate(input_line[:-1])}
last = input_line[-1]

for i in range(len(input_line), 30000000):
    if last in visited:
        current = i - visited[last]
    else:
        current = 0
    visited[last] = i
    last = current

print(last)
