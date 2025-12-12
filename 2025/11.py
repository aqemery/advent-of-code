import sys


def part1(graph):
    dp = {}

    def dfs(node):
        if node == "out":
            return 1
        if node in dp:
            return dp[node]
        if node not in graph:
            return 0

        total = sum(dfs(neighbor) for neighbor in graph[node])
        dp[node] = total
        return total

    return dfs("you")


def part2(graph):
    dp = {}
    must_visit = {"dac", "fft"}

    def dfs(node, seen_required):
        # Update seen_required if current node is required
        if node in must_visit:
            seen_required = seen_required | {node}

        seen_key = frozenset(seen_required)

        if (node, seen_key) in dp:
            return dp[(node, seen_key)]

        if node == "out":
            # Only count if we've seen all required nodes
            result = 1 if seen_required == must_visit else 0
            dp[(node, seen_key)] = result
            return result

        if node not in graph:
            return 0

        total = sum(dfs(neighbor, seen_required) for neighbor in graph[node])
        dp[(node, seen_key)] = total
        return total

    return dfs("svr", set())


if __name__ == "__main__":
    graph = {}
    for line in sys.stdin.read().split("\n"):
        node, neighbors = line.split(": ")
        graph[node] = neighbors.split()

    print("part 1:", part1(graph))
    print("part 2:", part2(graph))
