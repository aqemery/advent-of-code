#!/usr/bin/env python3
"""Advent of Code 2018 - Day 4: Repose Record"""

import re
from collections import defaultdict

def solve():
    with open('/Users/adamemery/advent-of-code/2018/input4', 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    # Sort lines chronologically
    lines.sort()

    # Parse and track sleep patterns
    guard_sleep = defaultdict(lambda: [0] * 60)  # guard_id -> minute counts

    current_guard = None
    sleep_start = None

    for line in lines:
        # Extract timestamp
        match = re.match(r'\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] (.+)', line)
        if not match:
            continue

        minute = int(match.group(5))
        action = match.group(6)

        if 'Guard' in action:
            guard_match = re.search(r'#(\d+)', action)
            current_guard = int(guard_match.group(1))
        elif 'falls asleep' in action:
            sleep_start = minute
        elif 'wakes up' in action:
            for m in range(sleep_start, minute):
                guard_sleep[current_guard][m] += 1

    # Part 1: Guard with most total sleep * their most slept minute
    total_sleep = {guard: sum(minutes) for guard, minutes in guard_sleep.items()}
    sleepiest_guard = max(total_sleep, key=total_sleep.get)
    sleepiest_minute = guard_sleep[sleepiest_guard].index(max(guard_sleep[sleepiest_guard]))
    part1 = sleepiest_guard * sleepiest_minute

    # Part 2: Guard most frequently asleep on the same minute
    max_frequency = 0
    part2_guard = None
    part2_minute = None

    for guard, minutes in guard_sleep.items():
        max_min_freq = max(minutes)
        if max_min_freq > max_frequency:
            max_frequency = max_min_freq
            part2_guard = guard
            part2_minute = minutes.index(max_min_freq)

    part2 = part2_guard * part2_minute

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    solve()
