from intcode import IntCode
from collections import defaultdict

DEFAULT_INPUT = 'day11.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        memory = list(map(int, f.readline().rstrip().split(',')))
    grid = defaultdict(int)
    coord = (0, 0)
    direction = (0, -1)
    painted = set()
    ic = IntCode(memory, 0)
    while True:
        new_color = ic.get_output()
        if new_color[0]:
            break
        grid[coord] = new_color[1]
        painted.add(coord)
        turn = ic.get_output()
        if turn[0]:
            break
        direction = new_direction(direction, turn[1])
        coord = coord[0] + direction[0], coord[1] + direction[1]
        ic.set_input(grid[coord])
    return len(painted)

def new_direction(current, turn):
    x, y = current
    if turn == 1:
        return -1 * y, x
    return y, -1 * x
    
        
def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        memory = list(map(int, f.readline().rstrip().split(',')))
    grid = defaultdict(int)
    coord = (0, 0)
    grid[(0, 0)] = 1
    direction = (0, -1)
    ic = IntCode(memory, 1)
    while True:
        new_color = ic.get_output()
        if new_color[0]:
            break
        grid[coord] = new_color[1]
        turn = ic.get_output()
        if turn[0]:
            break
        direction = new_direction(direction, turn[1])
        coord = coord[0] + direction[0], coord[1] + direction[1]
        ic.set_input(1 if grid[coord] else 0)
    min_x = min(grid.keys(), key=lambda p:p[0])[0]
    min_y = min(grid.keys(), key=lambda p:p[1])[1]
    max_x = max(grid.keys(), key=lambda p:p[0])[0]
    max_y = max(grid.keys(), key=lambda p:p[1])[1]
    rows = []
    for y in range(min_y, max_y + 1):
        row = ''
        for x in range(min_x, max_x + 1):
            if grid[(x, y)]:
                row += '#'
            else:
                row += ' '
        rows.append(row)
    print('\n'.join(rows))
        
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    part_2()
