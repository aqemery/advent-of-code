data = input()
i = 0
canceled = ""
while i < len(data):
    if data[i] == "!":
        i += 2
        continue
    canceled += data[i]
    i += 1

data = canceled

garbage_total = 0
i = 0
cleaned = ""
while i < len(data):
    if data[i] == "<":
        garbage_total -= 1
        while data[i] != ">":
            i += 1
            garbage_total += 1
    else:
        cleaned += data[i]
    i += 1

data = cleaned.replace(",", "")
total = 0
value = 1
for c in data:
    if c == "{":
        total += value
        value += 1
    elif c == "}":
        value -= 1

print("part 1:", total)
print("part 2:", garbage_total)
