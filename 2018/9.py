#!/usr/bin/env python3
"""Advent of Code 2018 Day 9: Marble Mania"""

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = self
        self.next = self

def play_game(num_players, last_marble):
    scores = [0] * num_players

    # Use doubly linked list for efficient insertions/removals
    current = Node(0)

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            player = (marble - 1) % num_players
            scores[player] += marble

            # Move 7 counter-clockwise
            for _ in range(7):
                current = current.prev

            # Remove current marble and add to score
            scores[player] += current.value

            # Update links
            current.prev.next = current.next
            current.next.prev = current.prev
            current = current.next
        else:
            # Insert between 1 and 2 clockwise from current
            left = current.next
            right = left.next

            new_node = Node(marble)
            new_node.prev = left
            new_node.next = right
            left.next = new_node
            right.prev = new_node
            current = new_node

    return max(scores)

def solve():
    with open('input9') as f:
        line = f.read().strip()

    # Parse "419 players; last marble is worth 71052 points"
    parts = line.split()
    num_players = int(parts[0])
    last_marble = int(parts[6])

    part1 = play_game(num_players, last_marble)
    part2 = play_game(num_players, last_marble * 100)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == '__main__':
    solve()
