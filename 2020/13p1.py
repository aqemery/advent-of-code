after = int(input())
buses = [int(i) for i in input().split(",") if i != "x"]
time = [((after // b + 1) * b, b) for b in buses]
bus = min(time)
print((bus[0] - after) * bus[1])
