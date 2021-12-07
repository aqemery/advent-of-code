from collections import deque

q = deque([0]*9)
for n in map(int,input().split(',')):
  q[n]+=1

for _ in range(80):
  b = q.popleft()
  q[6] += b
  q.append(b)

print(sum(q))
