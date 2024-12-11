from collections import defaultdict

input_stones = [x for x in input().split(" ")]


def solve(times):
    stones = defaultdict(int, {x: 1 for x in input_stones})
    for _ in range(times):
        next_stones = defaultdict(int)
        for s, count in stones.items():
            if s == "0":
                next_stones["1"] += count
            elif len(s) % 2 == 0:
                half = len(s) // 2
                next_stones[s[:half]] += count
                next_stones[str(int(s[half:]))] += count
            else:
                next_stones[str(int(s) * 2024)] += count

        stones = next_stones
    return sum(stones.values())


print("p1:", solve(25))
print("p2:", solve(75))
