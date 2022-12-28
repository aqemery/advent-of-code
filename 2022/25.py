import sys

if __name__ == "__main__":
    d = sys.stdin.read().split("\n")
    total = 0
    for line in d:
        number = ""
        minus = ""
        for c in line:
            if c == "-":
                number += "0"
                minus += "1"
            elif c == "=":
                number += "0"
                minus += "2"
            else:
                minus += "0"
                number += c

        total += int(number, 5) - int(minus, 5)

    snafu = []
    while total:
        snafu.append(total % 5)
        total //= 5

    snafu.reverse()

    while any(n > 2 for n in snafu):
        next_snafu = []
        for n in snafu:
            if n <= 2:
                next_snafu.append(n)
            else:
                next_snafu[-1] += 1
                next_snafu.append(n - 5)
        snafu = next_snafu
    
    out = ""
    for n in snafu:
        if n == -1:
            out += "-"
        elif n == -2:
            out += "="
        else:
            out += str(n)

    print("DONE:", out)