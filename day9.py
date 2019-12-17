from intcode import IntCode

DEFAULT_INPUT = 'day9.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        memory = list(map(int, f.readline().rstrip().split(',')))
    ic = IntCode(memory, 1)
    return ic.run_through()[0]
        
def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        memory = list(map(int, f.readline().rstrip().split(',')))
    ic = IntCode(memory, 2)
    return ic.run_through()[0]  
        
    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
