from intcode_generator import IntCode
from collections import defaultdict, deque

DEFAULT_INPUT = 'day23.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        memory = list(map(int, f.readline().rstrip().split(',')))
    computers = []
    for n in range(50):
        comp = IntCode(memory)
        comp.gen.send(n)
        computers.append(comp)
    messages = defaultdict(deque)
    while True:
        for i, comp in enumerate(computers):
            to_send = messages[i].popleft() if messages[i] else -1
            dest = comp.gen.send(to_send)
            if dest:
                x = next(comp.gen)
                y = next(comp.gen)
                if dest == 255:
                    return y
                messages[dest].append(x)
                messages[dest].append(y)
    

def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        memory = list(map(int, f.readline().rstrip().split(',')))
    computers = []
    for n in range(50):
        comp = IntCode(memory)
        comp.gen.send(n)
        computers.append(comp)
    messages = defaultdict(deque)
    nat = None
    prev_y = None
    since_last_packet = 0
    while True:
        if since_last_packet > 100:
            messages[0].append(nat[0])
            messages[0].append(nat[1])
            if nat[1] == prev_y:
                return prev_y
            prev_y = nat[1]
            since_last_packet = 0
        for i, comp in enumerate(computers):
            to_send = messages[i][0] if messages[i] else -1
            if comp.last_input == to_send:
                to_send = messages[i].popleft() if messages[i] else -1
                to_send = messages[i][0] if messages[i] else -1
            dest = comp.gen.send(to_send)
            if dest:
                x = next(comp.gen)
                y = next(comp.gen)
                if dest == 255:
                    nat = x, y
                else:
                    messages[dest].append(x)
                    messages[dest].append(y)
                since_last_packet = 0
            else:
                since_last_packet += 1
    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
