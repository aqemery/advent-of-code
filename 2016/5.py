import hashlib

door_id = "ojvtpuvg"


def part1():
    code = ""
    i = 0
    while len(code) < 8:
        hash_code = f"{door_id}{i}".encode("utf-8")
        hex = hashlib.md5(hash_code).hexdigest()
        if hex.startswith("00000"):
            code += hex[5]
        i += 1
    return code


def part2():
    code = {}
    i = 0
    while len(code) < 8:
        hash_code = f"{door_id}{i}".encode("utf-8")
        hex = hashlib.md5(hash_code).hexdigest()
        if hex.startswith("00000"):
            if hex[5] in "01234567" and hex[5] not in code:
                code[hex[5]] = hex[6]
        i += 1

    sorted_code = sorted(code.items(), key=lambda x: x[0])
    return "".join([v for _, v in sorted_code])


if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())
