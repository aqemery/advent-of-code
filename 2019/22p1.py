count = 10007
deck = [i for i in range(count)]


def increment(v):
    temp = [0] * count
    i = 0
    for c in deck:
        temp[i] = c
        i += v
        if i >= count:
            i -= count
    return temp


def cut(v):
    return deck[v:] + deck[:v]


def new_stack():
    return deck[::-1]


def get_value(c):
    return int(c.split(" ")[-1])


while True:
    try:
        command = input()
        if "increment" in command:
            deck = increment(get_value(command))
        elif "cut" in command:
            deck = cut(get_value(command))
        else:
            deck = new_stack()
    except EOFError:
        break

print(deck.index(2019))
