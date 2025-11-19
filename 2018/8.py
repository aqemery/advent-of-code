#!/usr/bin/env python3
"""Advent of Code 2018 Day 8: Memory Maneuver"""

def parse_node(data, index):
    """Parse a node and return (metadata_sum, value, new_index)"""
    num_children = data[index]
    num_metadata = data[index + 1]
    index += 2

    child_values = []
    total_metadata = 0

    # Parse children
    for _ in range(num_children):
        child_meta, child_val, index = parse_node(data, index)
        total_metadata += child_meta
        child_values.append(child_val)

    # Parse metadata
    metadata = data[index:index + num_metadata]
    index += num_metadata
    total_metadata += sum(metadata)

    # Calculate value
    if num_children == 0:
        value = sum(metadata)
    else:
        value = 0
        for m in metadata:
            if 1 <= m <= len(child_values):
                value += child_values[m - 1]

    return total_metadata, value, index

def solve():
    with open('input8') as f:
        data = list(map(int, f.read().split()))

    metadata_sum, root_value, _ = parse_node(data, 0)

    print(f"Part 1: {metadata_sum}")
    print(f"Part 2: {root_value}")

if __name__ == '__main__':
    solve()
