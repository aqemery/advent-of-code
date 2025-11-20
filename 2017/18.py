from collections import defaultdict, deque

def parse(filename):
    with open(filename) as f:
        return [line.strip().split() for line in f]

def get_val(regs, x):
    try:
        return int(x)
    except:
        return regs[x]

def part1(instructions):
    regs = defaultdict(int)
    last_sound = 0
    ip = 0

    while 0 <= ip < len(instructions):
        cmd = instructions[ip]
        op = cmd[0]

        if op == 'snd':
            last_sound = get_val(regs, cmd[1])
        elif op == 'set':
            regs[cmd[1]] = get_val(regs, cmd[2])
        elif op == 'add':
            regs[cmd[1]] += get_val(regs, cmd[2])
        elif op == 'mul':
            regs[cmd[1]] *= get_val(regs, cmd[2])
        elif op == 'mod':
            regs[cmd[1]] %= get_val(regs, cmd[2])
        elif op == 'rcv':
            if get_val(regs, cmd[1]) != 0:
                return last_sound
        elif op == 'jgz':
            if get_val(regs, cmd[1]) > 0:
                ip += get_val(regs, cmd[2])
                continue
        ip += 1

    return last_sound

def part2(instructions):
    regs = [defaultdict(int), defaultdict(int)]
    regs[0]['p'] = 0
    regs[1]['p'] = 1

    queues = [deque(), deque()]
    ip = [0, 0]
    waiting = [False, False]
    send_count = 0

    while True:
        if waiting[0] and waiting[1]:
            break
        if (ip[0] < 0 or ip[0] >= len(instructions)) and (ip[1] < 0 or ip[1] >= len(instructions)):
            break

        for prog in [0, 1]:
            if ip[prog] < 0 or ip[prog] >= len(instructions):
                waiting[prog] = True
                continue

            cmd = instructions[ip[prog]]
            op = cmd[0]

            if op == 'snd':
                val = get_val(regs[prog], cmd[1])
                queues[1 - prog].append(val)
                if prog == 1:
                    send_count += 1
                waiting[prog] = False
            elif op == 'set':
                regs[prog][cmd[1]] = get_val(regs[prog], cmd[2])
                waiting[prog] = False
            elif op == 'add':
                regs[prog][cmd[1]] += get_val(regs[prog], cmd[2])
                waiting[prog] = False
            elif op == 'mul':
                regs[prog][cmd[1]] *= get_val(regs[prog], cmd[2])
                waiting[prog] = False
            elif op == 'mod':
                regs[prog][cmd[1]] %= get_val(regs[prog], cmd[2])
                waiting[prog] = False
            elif op == 'rcv':
                if queues[prog]:
                    regs[prog][cmd[1]] = queues[prog].popleft()
                    waiting[prog] = False
                else:
                    waiting[prog] = True
                    continue
            elif op == 'jgz':
                if get_val(regs[prog], cmd[1]) > 0:
                    ip[prog] += get_val(regs[prog], cmd[2])
                    continue
                waiting[prog] = False

            ip[prog] += 1

    return send_count

if __name__ == '__main__':
    instructions = parse('/Users/adamemery/advent-of-code/2017/input18')
    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")
