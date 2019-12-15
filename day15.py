from intcode import IntCode
from collections import deque

DEFAULT_INPUT = 'day15.txt'

def day_15(loc=DEFAULT_INPUT):
    with open(loc) as f:
        instructions = list(map(int, f.readline().rstrip().split(',')))
    grid = {(0, 0): '.', (1, 0): '?', (-1, 0): '?', (0, 1): '?', (0, -1): '?'}
    droid = (0, 0)
    move_to_dir = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}
    ic = IntCode(instructions)
    while '?' in grid.values():
        path = find_nearest_unknown(grid, droid)
        for m in path[:-1]:
            ic.set_input(m)
            ic.get_output()
            droid = (droid[0] + move_to_dir[m][0], droid[1] + move_to_dir[m][1])
        m = path[-1]
        ic.set_input(m)
        status = ic.get_output()[1]
        if status == 0:
            wall = (droid[0] + move_to_dir[m][0], droid[1] + move_to_dir[m][1])
            grid[wall] = '#'
        else:
            droid = (droid[0] + move_to_dir[m][0], droid[1] + move_to_dir[m][1])
            if status == 1:
                grid[droid] = '.'
            else:
                grid[droid] = 'O'
                target = droid
            for adj_cell, _ in adjacent(droid):
                if adj_cell not in grid:
                    grid[adj_cell] = '?'
    p1_res = shortest_path(grid, (0, 0), target)
    time = 0
    with_oxygen = [target]
    while '.' in grid.values():
        new_oxygen = []
        for cell in with_oxygen:
            all_adj = adjacent(cell)
            for adj_cell, _ in all_adj:
                if grid[adj_cell] == '.':
                    grid[adj_cell] = 'O'
                    new_oxygen.append(adj_cell)
        with_oxygen = new_oxygen
        time += 1
    return p1_res, time
        
def draw(grid):
    min_x = min(grid.keys(), key=lambda p:p[0])[0]
    min_y = min(grid.keys(), key=lambda p:p[1])[1]
    max_x = max(grid.keys(), key=lambda p:p[0])[0]
    max_y = max(grid.keys(), key=lambda p:p[1])[1]
    rows = []
    for y in range(min_y, max_y + 1):
        row = ''
        for x in range(min_x, max_x + 1):
            if (x, y) not in grid:
                row += ' '
            else:
                row += grid[(x, y)]
        rows.append(row)
    print('\n'.join(rows))

def adjacent(cell):
    x, y = cell
    return [((x + 1, y), 4), ((x - 1, y), 3),
            ((x, y + 1), 2), ((x, y - 1), 1)]

def find_nearest_unknown(grid, current_loc):
    seen = set([current_loc])
    d = deque([(current_loc, [])])
    while d:
        current_loc, current_path = d.popleft()
        all_adj = adjacent(current_loc)
        for adj_cell, adj_dir in all_adj:
            if grid[adj_cell] == '#' or adj_cell in seen:
                continue
            if grid[adj_cell] == '?':
                return current_path + [adj_dir]
            seen.add(adj_cell)
            d.append((adj_cell, current_path + [adj_dir]))

def shortest_path(grid, start, end):
    seen = set([start])
    d = deque([(start, 0)])
    while d:
        current_loc, current_len = d.popleft()
        all_adj = adjacent(current_loc)
        for adj_cell, _ in all_adj:
            if grid[adj_cell] == '#' or adj_cell in seen:
                continue
            if adj_cell == end:
                return current_len + 1
            seen.add(adj_cell)
            d.append((adj_cell, current_len + 1))
        
if __name__ == '__main__':
    res = day_15()
    print(f'Solution for Part One: {res[0]}\nSolution for Part Two: {res[1]}')
