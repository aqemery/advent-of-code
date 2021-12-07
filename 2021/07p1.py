from statistics import median
crabs = list(map(int,input().split(',')))
med = int(median(crabs))
print(sum([abs(med-c) for c in crabs]))

