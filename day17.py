from intcode import IntCode
from collections import defaultdict

DEFAULT_INPUT = 'day17.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        memory = list(map(int, f.readline().rstrip().split(',')))
    ic = IntCode(memory)
    asc = ic.run_through()
    grid = defaultdict(lambda:'.')
    y = 0
    x = 0
    scaffolds = set()
    max_x = 0
    max_y = 0
    for n in asc:
        if n == 10:
            x = 0
            y += 1
            max_y = max(max_y, y)
        else:
            c = chr(n)
            grid[(x,y)] = c
            if c in '#^v<>':
                scaffolds.add((x, y))
            if c == '^':
                start = (x, y)
                start_dir = (0, -1)
            elif c == 'v':
                start = (x, y)
                start_dir = (0, 1)
            elif c == '>':
                start = (x, y)
                start_dir = (1, 0)
            elif c == '<':
                start = (x, y)
                start_dir = (-1, 0)
            x += 1
            max_x = max(max_x, x)
    res = 0
    for x,y in scaffolds:
        if (x + 1, y) in scaffolds and (x - 1, y) in scaffolds and \
           (x, y + 1) in scaffolds and (x, y - 1) in scaffolds:
            res += x * y
    path = find_path(grid, start, start_dir)
    return res, path

def draw(grid, max_x, max_y):
    rows = []
    for y in range(max_y + 1):
        row = ''
        for x in range(max_x + 1):
            row += grid[(x,y)]
        rows.append(row)
    print('\n'.join(rows))

def find_path(grid, start, start_dir):
    def turn_right(dx, dy):
        return -dy, dx
    def turn_left(dx, dy):
        return dy, -dx
    def next_space(x, y, dx, dy):
        return grid[(x + dx, y + dy)]
    path = []
    spaces = 0
    x, y = start
    dx, dy = start_dir
    while True:
        if next_space(x, y, dx, dy) == '#':
            x += dx
            y += dy
            spaces += 1
        elif next_space(x, y, *turn_left(dx, dy)) == '#':
            dx, dy = turn_left(dx, dy)
            if spaces != 0:
                path.append(str(spaces))
                spaces = 0
            path.append('L')
        elif next_space(x, y, *turn_right(dx, dy)) == '#':
            dx, dy = turn_right(dx, dy)
            if spaces != 0:
                path.append(str(spaces))
                spaces = 0
            path.append('R')
        else:
            if spaces != 0:
                path.append(str(spaces))
            break
    return ','.join(path)
    
def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        memory = list(map(int, f.readline().rstrip().split(',')))
    #moves solved by hand for given input
    moves = 'A,B,A,A,B,C,B,C,C,B'
    func_a = 'L,12,R,8,L,6,R,8,L,6'
    func_b = 'R,8,L,12,L,12,R,8'
    func_c = 'L,6,R,6,L,12'
    memory[0] = 2
    ic = IntCode(memory)
    ic.add_ascii_inputs(moves)
    ic.add_ascii_inputs(func_a)
    ic.add_ascii_inputs(func_b)
    ic.add_ascii_inputs(func_c)
    ic.add_ascii_inputs('n')
    return ic.run_through()[-1]
        
if __name__ == '__main__':
    p1 = part_1()
    print(f'Solution for Part One: {p1[0]}\nIntial path for Part Two: {p1[1]}')
    print('Solution for Part Two:', part_2())
