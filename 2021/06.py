from collections import deque


def solve(nums, days):
    q = deque([0] * 9)
    for n in nums:
        q[n] += 1

    for _ in range(days):
        b = q.popleft()
        q[6] += b
        q.append(b)
    return sum(q)


if __name__ == "__main__":
    nums = list(map(int, input().split(",")))
    print("part 1:", solve(nums, 80))
    print("part 2:", solve(nums, 256))
