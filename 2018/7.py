#!/usr/bin/env python3
"""Advent of Code 2018 Day 7: The Sum of Its Parts"""

import re
from collections import defaultdict
import heapq

def solve():
    with open('input7') as f:
        lines = f.read().strip().split('\n')

    # Parse dependencies
    # "Step X must be finished before step Y can begin."
    pattern = r'Step (\w) must be finished before step (\w) can begin'

    deps = defaultdict(set)  # deps[step] = set of steps that must come before it
    all_steps = set()

    for line in lines:
        match = re.search(pattern, line)
        if match:
            before, after = match.groups()
            deps[after].add(before)
            all_steps.add(before)
            all_steps.add(after)

    # Part 1: Topological sort with alphabetical priority
    remaining_deps = {step: set(deps[step]) for step in all_steps}
    result = []
    available = []

    # Find initial available steps (no dependencies)
    for step in all_steps:
        if not remaining_deps[step]:
            heapq.heappush(available, step)

    while available:
        # Take alphabetically first available step
        step = heapq.heappop(available)
        result.append(step)

        # Remove this step from dependencies
        for s in remaining_deps:
            if step in remaining_deps[s]:
                remaining_deps[s].remove(step)
                if not remaining_deps[s] and s not in result and s not in available:
                    heapq.heappush(available, s)

    part1 = ''.join(result)

    # Part 2: 5 workers, step time = 60 + letter position
    num_workers = 5
    base_time = 60

    remaining_deps = {step: set(deps[step]) for step in all_steps}
    completed = set()
    in_progress = {}  # step -> finish_time
    time = 0

    while len(completed) < len(all_steps):
        # Check for completed tasks
        newly_completed = [step for step, finish in in_progress.items() if finish <= time]
        for step in newly_completed:
            completed.add(step)
            del in_progress[step]
            # Remove from dependencies
            for s in remaining_deps:
                remaining_deps[s].discard(step)

        # Find available steps
        available = []
        for step in all_steps:
            if step not in completed and step not in in_progress:
                if not remaining_deps[step]:
                    available.append(step)
        available.sort()

        # Assign workers
        while len(in_progress) < num_workers and available:
            step = available.pop(0)
            duration = base_time + ord(step) - ord('A') + 1
            in_progress[step] = time + duration

        # Advance time
        if in_progress:
            time = min(in_progress.values())
        else:
            break

    part2 = time

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == '__main__':
    solve()
