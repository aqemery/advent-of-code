from collections import defaultdict

def parse(filename):
    with open(filename) as f:
        return [int(line.strip()) for line in f if line.strip()]

def next_secret(s):
    s = ((s * 64) ^ s) % 16777216
    s = ((s // 32) ^ s) % 16777216
    s = ((s * 2048) ^ s) % 16777216
    return s

def part1(secrets):
    total = 0
    for s in secrets:
        for _ in range(2000):
            s = next_secret(s)
        total += s
    return total

def part2(secrets):
    sequence_totals = defaultdict(int)

    for initial in secrets:
        s = initial
        prices = [s % 10]
        for _ in range(2000):
            s = next_secret(s)
            prices.append(s % 10)

        changes = [prices[i] - prices[i-1] for i in range(1, len(prices))]

        seen = set()
        for i in range(len(changes) - 3):
            seq = tuple(changes[i:i+4])
            if seq not in seen:
                seen.add(seq)
                sequence_totals[seq] += prices[i + 4]

    return max(sequence_totals.values())

if __name__ == '__main__':
    secrets = parse('/Users/adamemery/advent-of-code/2024/input22')
    print(f"Part 1: {part1(secrets)}")
    print(f"Part 2: {part2(secrets)}")
