import math

bits = "".join([f"{int(c,16):04b}" for c in input()])
p = 0

ops = {
    0: sum,
    1: math.prod,
    2: min,
    3: max,
    5: lambda x: int(x[0] > x[1]),
    6: lambda x: int(x[0] < x[1]),
    7: lambda x: int(x[0] == x[1]),
}


def read_bits(x):
    global p
    p += x
    return bits[p - x : p]


def read_int(x):
    return int(read_bits(x), 2)


def read_packet():
    read_int(3)
    id = read_int(3)
    if id == 4:
        return read_literal()
    else:
        return read_operator(id)


def read_literal():
    packet = ""
    while read_int(1):
        packet += read_bits(4)
    packet += read_bits(4)
    return int(packet, 2)


def read_operator(op):
    if read_int(1):
        paks = [read_packet() for _ in range(read_int(11))]
    else:
        length = read_int(15)
        cp = p
        paks = []
        while p - cp < length:
            paks.append(read_packet())
    return ops[op](paks)


print(read_packet())
