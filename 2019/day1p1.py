allFuel = [] 
while True:
  try:
    x = int(input())
    x //= 3
    x -= 2
    allFuel.append(x)
  except EOFError:
    break

print(sum(allFuel))
