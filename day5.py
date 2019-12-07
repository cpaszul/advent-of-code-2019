from intcode import IntCode

DEFAULT_INPUT = 'day5.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        instructions = list(map(int, f.readline().rstrip().split(',')))
    return IntCode(instructions, 1).run_through()[-1]
        
def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        instructions = list(map(int, f.readline().rstrip().split(',')))
    return IntCode(instructions, 5).run_through()[0]
    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
