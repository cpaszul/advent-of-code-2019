from intcode import IntCode

DEFAULT_INPUT = 'day21.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        memory = list(map(int, f.readline().rstrip().split(',')))
    #jump if (not A) or (not C and D)
    instructions = ['OR A J',
                    'AND C J',
                    'NOT J J',
                    'AND D J',
                    'WALK']
    ic = IntCode(memory)
    for inst in instructions:
        ic.add_ascii_inputs(inst)
    return ic.run_through()[-1]
        

def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        memory = list(map(int, f.readline().rstrip().split(',')))
    instructions = ['OR A J',
                    'AND B J',
                    'AND C J',
                    'NOT J J',
                    'OR E T',
                    'OR H T',
                    'AND T J',
                    'AND D J',
                    'RUN']
    ic = IntCode(memory)
    for inst in instructions:
        ic.add_ascii_inputs(inst)
    return ic.run_through()[-1]
    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
