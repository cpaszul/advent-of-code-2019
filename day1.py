DEFAULT_INPUT = 'day1.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        return sum(int(line.rstrip())//3 - 2 for line in f.readlines())

def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        return sum(fuel_needed(int(line.rstrip())) for line in f.readlines())
    
def fuel_needed(n):
    f = n//3 - 2
    if f > 0:
        return f + fuel_needed(f)
    return 0

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
