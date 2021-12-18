dimensions = input().split(",")[-2:]
_, ry = [map(int, dem.split("=")[1].split("..")) for dem in dimensions]
y = min(ry)
print(y * (y + 1) // 2)
