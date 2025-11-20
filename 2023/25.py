from collections import defaultdict, deque
import random

def parse(filename):
    graph = defaultdict(set)
    with open(filename) as f:
        for line in f:
            if line.strip():
                parts = line.strip().replace(':', '').split()
                node = parts[0]
                for neighbor in parts[1:]:
                    graph[node].add(neighbor)
                    graph[neighbor].add(node)
    return graph

def bfs_path(graph, start, end):
    """Find a path from start to end using BFS."""
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

def count_component(graph, start):
    """Count nodes in connected component containing start."""
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    return len(visited)

def find_min_cut(graph):
    """Find the 3 edges to cut using edge frequency in random paths."""
    nodes = list(graph.keys())
    edge_count = defaultdict(int)

    # Sample random paths and count edge usage
    for _ in range(200):
        a, b = random.sample(nodes, 2)
        path = bfs_path(graph, a, b)
        if path:
            for i in range(len(path) - 1):
                edge = tuple(sorted([path[i], path[i + 1]]))
                edge_count[edge] += 1

    # Most used edges are likely the bridge edges
    top_edges = sorted(edge_count.items(), key=lambda x: -x[1])[:3]

    # Remove these edges and check if we get two components
    for (a, b), _ in top_edges:
        graph[a].remove(b)
        graph[b].remove(a)

    # Count component sizes
    start = nodes[0]
    size1 = count_component(graph, start)
    size2 = len(nodes) - size1

    return size1 * size2

def part1(graph):
    # Make a copy since we'll modify it
    graph_copy = defaultdict(set)
    for node, neighbors in graph.items():
        graph_copy[node] = neighbors.copy()

    return find_min_cut(graph_copy)

if __name__ == '__main__':
    graph = parse('/Users/adamemery/advent-of-code/2023/input25')
    print(f"Part 1: {part1(graph)}")
    print(f"Part 2: (free star)")
