import math

crabs = list(map(int,input().split(',')))
average = math.floor(sum(crabs)/len(crabs))
print(sum([sum(range(1,abs(average-c)+1)) for c in crabs]))
