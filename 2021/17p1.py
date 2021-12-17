rx, ry = [map(int, dem.split('=')[1].split('..')) for dem in input().split(',')[-2:]]
y = min(ry)
print(y*(y+1)//2)
