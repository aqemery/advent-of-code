lines = []
while True:
  try:
    lines.append(input())
  except EOFError:
    break

width = len(lines[0])
height = len(lines)

tree_count = 0
x = 0
for y in range(0,height):
  if lines[y][x % width] == '#':
    tree_count += 1
  x += 3

print(tree_count)
