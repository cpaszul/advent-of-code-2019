from intcode import IntCode

DEFAULT_INPUT = 'day19.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        memory = list(map(int, f.readline().rstrip().split(',')))
    s = 0
    for x in range(50):
        for y in range(50):
            ic = IntCode(memory.copy(), x, y)
            if ic.get_output()[1] == 1:
                s += 1
    return s
        
def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        memory = list(map(int, f.readline().rstrip().split(',')))
    x = 0
    y = 99
    while True:
        ic = IntCode(memory.copy(), x, y)
        if ic.get_output()[1] == 0:
            x += 1
        else:
            if IntCode(memory.copy(), x + 99, y - 99).get_output()[1] == 1:
                return x * 10000 + (y - 99)
            y += 1
        
    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
