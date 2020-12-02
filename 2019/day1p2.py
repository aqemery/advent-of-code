def calc_fuel(mass):
  fuel = mass // 3
  fuel -= 2
  return fuel if fuel > 0 else 0

allFuel = [] 
while True:
  try:
    mass = int(input())
    subFuel = []
    while mass != 0:
      mass = calc_fuel(mass)
      subFuel.append(mass)
    allFuel.append(sum(subFuel))
  except EOFError:
    break

print(sum(allFuel))
