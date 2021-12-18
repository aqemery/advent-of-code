lines = []
while True:
    try:
        lines.append(input())
    except EOFError:
        break

width = len(lines[0])
height = len(lines)

slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
trees = []
for s in slopes:
    tree_count = 0
    x = 0
    for y in range(0, height, s[0]):
        if lines[y][x % width] == "#":
            tree_count += 1
        x += s[1]
    trees.append(tree_count)

product = trees[0]

for t in trees[1:]:
    product *= t

print(product)
