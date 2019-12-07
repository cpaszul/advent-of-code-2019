from intcode import IntCode

DEFAULT_INPUT = 'day2.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        ints = list(map(int, f.readline().rstrip().split(',')))
    return run_program(ints, 12, 2)

def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        ints = list(map(int, f.readline().rstrip().split(',')))
    for n in range(100):
        for v in range(100):
            res = run_program(ints, n, v)
            if res == 19690720:
                return 100 * n + v

def run_program(base_ints, noun, verb):
    ints = base_ints.copy()
    ints[1] = noun
    ints[2] = verb
    ic = IntCode(ints)
    ic.run_through()
    return ic.instructions[0]
    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
