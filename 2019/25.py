from itertools import combinations
from collections import deque
import re


class Computer:
    def __init__(self, program):
        self.program = program
        self.memory = program.copy() + [0] * 10000
        self.pointer = 0
        self.relative = 0
        self.halted = False

    def get_params(self, instruct, *rw):
        param_modes = list(map(int, instruct[:-2]))
        param_modes.reverse()
        count = len(rw)
        params = [self.memory[self.pointer + i] for i in range(1, count + 1)]
        for i in range(len(param_modes)):
            if i >= count:
                break
            if rw[i]:
                if param_modes[i] == 0 and len(params) > i:
                    params[i] = params[i]
                elif param_modes[i] == 2 and len(params) > i:
                    params[i] = params[i] + self.relative
            else:
                if param_modes[i] == 0 and len(params) > i:
                    params[i] = self.memory[params[i]]
                elif param_modes[i] == 2 and len(params) > i:
                    params[i] = self.memory[params[i] + self.relative]
        self.pointer += count + 1
        if count == 1:
            return params[0]
        return params

    def run(self):
        while True:
            instruct = f"{self.memory[self.pointer]:04d}"
            opcode = int(instruct[-2:])
            if opcode in [1, 2, 7, 8]:
                x, y, z = self.get_params(instruct, False, False, True)
                if opcode == 1:
                    self.memory[z] = x + y
                elif opcode == 2:
                    self.memory[z] = x * y
                elif opcode == 7:
                    self.memory[z] = 1 if x < y else 0
                elif opcode == 8:
                    self.memory[z] = 1 if x == y else 0
            elif opcode == 3:
                self.memory[self.get_params(instruct, True)] = yield
            elif opcode == 4:
                yield self.get_params(instruct, False)
            elif opcode == 9:
                self.relative += self.get_params(instruct, False)
            elif opcode in [5, 6]:
                x, y = self.get_params(instruct, False, False)
                if x != 0 and opcode == 5:
                    self.pointer = y
                elif x == 0 and opcode == 6:
                    self.pointer = y
            elif opcode == 99:
                self.halted = True
                break
            else:
                print("opcode error", opcode)
                break


class TextAdventure:
    def __init__(self, program):
        self.program = program
        self.reset()

    def reset(self):
        self.comp = Computer(self.program.copy())
        self.gen = self.comp.run()
        self.input_queue = []
        self.waiting_for_input = False

    def run_until_input_needed(self):
        """Run the program collecting output until it needs input or halts"""
        output = []
        try:
            while True:
                if self.waiting_for_input and self.input_queue:
                    char = self.input_queue.pop(0)
                    val = self.gen.send(char)
                    self.waiting_for_input = False
                elif self.waiting_for_input:
                    # Need input but don't have any
                    break
                else:
                    val = next(self.gen)

                if val is None:
                    # Yielded from input instruction, needs input
                    self.waiting_for_input = True
                else:
                    output.append(chr(val))
        except StopIteration:
            return ''.join(output), True

        return ''.join(output), False

    def send_command(self, command):
        """Send a command and get the output"""
        # Queue up the command
        for char in command + '\n':
            self.input_queue.append(ord(char))

        return self.run_until_input_needed()

    def get_initial_output(self):
        """Get the initial output from the game"""
        return self.run_until_input_needed()


def parse_room(text):
    """Parse room description to extract name, doors, and items"""
    room_name = None
    doors = []
    items = []

    # Extract room name
    name_match = re.search(r'== (.+) ==', text)
    if name_match:
        room_name = name_match.group(1)

    # Extract doors
    doors_match = re.search(r'Doors here lead:\n((?:- \w+\n)+)', text)
    if doors_match:
        doors = re.findall(r'- (\w+)', doors_match.group(1))

    # Extract items
    items_match = re.search(r'Items here:\n((?:- .+\n)+)', text)
    if items_match:
        items = re.findall(r'- (.+)', items_match.group(1))

    return room_name, doors, items


def get_opposite_direction(direction):
    """Get the opposite direction"""
    opposites = {
        'north': 'south',
        'south': 'north',
        'east': 'west',
        'west': 'east'
    }
    return opposites.get(direction)


def solve():
    # Load the program
    with open('/Users/adamemery/advent-of-code/2019/input25') as f:
        program = list(map(int, f.read().strip().split(',')))

    # Dangerous items to avoid
    dangerous_items = {
        'photons',
        'giant electromagnet',
        'escape pod',
        'infinite loop',
        'molten lava'
    }

    # First, explore the entire map to find all items and the security checkpoint
    game = TextAdventure(program)
    output, halted = game.get_initial_output()

    # DFS exploration
    visited = set()
    item_locations = {}  # item -> path to get there (not including take command)
    security_checkpoint_path = None
    checkpoint_direction = None

    def explore(path, came_from=None):
        nonlocal security_checkpoint_path, checkpoint_direction

        # Reset and navigate to this location
        game.reset()
        output, halted = game.get_initial_output()

        for cmd in path:
            output, halted = game.send_command(cmd)
            if halted:
                return

        room_name, doors, items = parse_room(output)

        if room_name is None:
            return

        if room_name in visited:
            return

        visited.add(room_name)

        # Record items
        for item in items:
            if item not in dangerous_items:
                item_locations[item] = path.copy()

        # Check for security checkpoint
        if room_name == 'Security Checkpoint':
            security_checkpoint_path = path.copy()
            # The direction to pressure sensor is the one that's not where we came from
            # and leads to "Pressure-Sensitive Floor"
            for door in doors:
                if get_opposite_direction(door) != came_from:
                    checkpoint_direction = door

        # Explore all directions
        for door in doors:
            opposite = get_opposite_direction(door)
            if opposite == came_from:
                continue
            explore(path + [door], door)

    explore([])

    # Now do a single run: collect all items, go to checkpoint, try combinations
    game.reset()
    output, halted = game.get_initial_output()

    collected = []

    def collect_and_explore(came_from=None):
        nonlocal output

        room_name, doors, items = parse_room(output)

        if room_name is None:
            return

        if room_name in visited:
            return

        visited.add(room_name)

        # Collect safe items in this room
        for item in items:
            if item not in dangerous_items:
                output, halted = game.send_command(f'take {item}')
                collected.append(item)

        # Explore all directions (but don't step on pressure sensor)
        for door in doors:
            opposite = get_opposite_direction(door)
            if opposite == came_from:
                continue

            # Don't step on the pressure sensor yet
            if room_name == 'Security Checkpoint':
                continue

            output, halted = game.send_command(door)
            if not halted:
                collect_and_explore(door)
                # Go back
                output, halted = game.send_command(opposite)

    visited = set()
    collect_and_explore()

    # Now navigate to security checkpoint
    # Reset and collect items again, then go to checkpoint
    game.reset()
    output, halted = game.get_initial_output()

    visited = set()
    collected = []

    def collect_all(came_from=None):
        nonlocal output

        room_name, doors, items = parse_room(output)
        if room_name is None:
            return

        if room_name in visited:
            return
        visited.add(room_name)

        # Collect items
        for item in items:
            if item not in dangerous_items:
                output, halted = game.send_command(f'take {item}')
                collected.append(item)

        for door in doors:
            opposite = get_opposite_direction(door)
            if opposite == came_from:
                continue
            if room_name == 'Security Checkpoint':
                continue

            output, halted = game.send_command(door)
            if not halted:
                collect_all(door)
                output, halted = game.send_command(opposite)

    collect_all()

    # Now go to security checkpoint
    if security_checkpoint_path:
        for cmd in security_checkpoint_path:
            output, halted = game.send_command(cmd)

    # Parse current room to verify we're at checkpoint and get direction
    room_name, doors, items = parse_room(output)

    if room_name != 'Security Checkpoint':
        # Need to find path to checkpoint from current position
        # Use BFS
        game.reset()
        output, halted = game.get_initial_output()

        # Collect all items first
        visited = set()
        collected = []
        collect_all()

        # Now BFS to checkpoint
        queue = deque()
        queue.append([])
        visited_bfs = set()

        while queue:
            path = queue.popleft()

            game.reset()
            output, halted = game.get_initial_output()

            # Collect items
            visited = set()
            collected = []
            collect_all()

            # Navigate
            for cmd in path:
                output, halted = game.send_command(cmd)

            room_name, doors, items = parse_room(output)
            if room_name is None:
                continue

            if room_name in visited_bfs:
                continue
            visited_bfs.add(room_name)

            if room_name == 'Security Checkpoint':
                break

            for door in doors:
                queue.append(path + [door])

    # We should be at security checkpoint now
    room_name, doors, items = parse_room(output)

    # Find the direction to the pressure sensor
    # It's the only unexplored direction (not where we came from)
    if security_checkpoint_path and len(security_checkpoint_path) > 0:
        came_from = get_opposite_direction(security_checkpoint_path[-1])
    else:
        came_from = None

    for door in doors:
        if door != came_from:
            checkpoint_direction = door
            break

    if checkpoint_direction is None:
        # Just try all doors
        checkpoint_direction = doors[0] if doors else 'north'

    # Drop all items
    for item in collected:
        output, halted = game.send_command(f'drop {item}')

    # Try all combinations of items
    answer = None
    for r in range(len(collected) + 1):
        if answer:
            break
        for combo in combinations(collected, r):
            # Pick up items
            for item in combo:
                output, halted = game.send_command(f'take {item}')

            # Try to pass
            output, halted = game.send_command(checkpoint_direction)

            # Check result
            if 'lighter' not in output and 'heavier' not in output:
                # Success! Find the number
                match = re.search(r'(\d+)', output)
                if match:
                    answer = match.group(1)
                    break

            # Drop items for next attempt
            for item in combo:
                output, halted = game.send_command(f'drop {item}')

        if answer:
            break

    return answer


if __name__ == '__main__':
    result = solve()
    print(f"Day 25: Part 1 = {result}, Part 2 = (free star)")
