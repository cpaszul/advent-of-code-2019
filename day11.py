from intcode import IntCode
from collections import defaultdict

DEFAULT_INPUT = 'day11.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        instructions = list(map(int, f.readline().rstrip().split(',')))
    grid = defaultdict(lambda:False)
    coord = (0, 0)
    direction = (0, -1)
    painted = set()
    ic = IntCode(instructions, 0)
    while True:
        new_color = ic.get_output()
        if new_color is True:
            break
        grid[coord] = new_color == True
        painted.add(coord)
        turn = ic.get_output()
        if turn is True:
            break
        direction = new_direction(direction, turn)
        coord = coord[0] + direction[0], coord[1] + direction[1]
        ic.set_input(1 if grid[coord] else 0)
    return len(painted)

def new_direction(current, turn):
    x, y = current
    if turn == 1:
        return -1 * y, x
    return y, -1 * x
    
        
def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        instructions = list(map(int, f.readline().rstrip().split(',')))
    grid = defaultdict(lambda:False)
    coord = (0, 0)
    grid[(0, 0)] = True
    direction = (0, -1)
    ic = IntCode(instructions, 1)
    while True:
        new_color = ic.get_output()
        if new_color is True:
            break
        grid[coord] = new_color == True
        turn = ic.get_output()
        if turn is True:
            break
        direction = new_direction(direction, turn)
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
