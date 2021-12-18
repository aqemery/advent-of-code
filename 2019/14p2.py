import math
import copy

bank = {}
plans = {}
while True:
    try:
        r = input().split(" => ")
        inpt = [[int(i.split(" ")[0]), i.split(" ")[1]] for i in r[0].split(", ")]
        out = r[1].split(" ")
        plans[out[1]] = [int(out[0]), inpt]
    except EOFError:
        break

current = list(plans["FUEL"][1])
ore = 0
index = 0
length = len(current)

ore = 1000000000000
fuel = 0

while ore > 0:
    current = list(plans["FUEL"][1])
    index = 0
    length = len(current)

    while index < len(current):
        needed, name = current[index]
        if name == "ORE":
            index += 1
            ore -= needed
        else:
            amount, elements = copy.deepcopy(plans[name])
            elements = elements.copy()
            multiplier = 1
            if name in bank:
                needed -= bank[name]
                del bank[name]

            if needed <= 0:
                current.pop(index)
                if needed < 0:
                    bank[name] = -needed
            else:
                if amount < needed:
                    multiplier = math.ceil(1 / (amount / needed))
                amount *= multiplier
                if multiplier != 1:
                    for e in elements:
                        e[0] *= multiplier

                current = current[:index] + elements + current[index + 1 :]
                length = len(current)

                if amount > needed:
                    bank[name] = amount - needed

    if ore >= 0:
        fuel += 1

print("fuel created", fuel)
