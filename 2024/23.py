from collections import defaultdict

def parse(filename):
    graph = defaultdict(set)
    with open(filename) as f:
        for line in f:
            if line.strip():
                a, b = line.strip().split('-')
                graph[a].add(b)
                graph[b].add(a)
    return graph

def part1(graph):
    triangles = set()
    for a in graph:
        for b in graph[a]:
            for c in graph[b]:
                if c in graph[a]:
                    triangles.add(tuple(sorted([a, b, c])))

    return sum(1 for t in triangles if any(n.startswith('t') for n in t))

def part2(graph):
    # Bron-Kerbosch algorithm for maximum clique
    def bron_kerbosch(r, p, x):
        if not p and not x:
            return r
        best = r
        for v in list(p):
            result = bron_kerbosch(
                r | {v},
                p & graph[v],
                x & graph[v]
            )
            if len(result) > len(best):
                best = result
            p = p - {v}
            x = x | {v}
        return best

    nodes = set(graph.keys())
    clique = bron_kerbosch(set(), nodes, set())
    return ','.join(sorted(clique))

if __name__ == '__main__':
    graph = parse('/Users/adamemery/advent-of-code/2024/input23')
    print(f"Part 1: {part1(graph)}")
    print(f"Part 2: {part2(graph)}")
