DEFAULT_INPUT = 'day24.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        lines = [line.rstrip() for line in f.readlines()]
    seen = {''.join(lines)}
    while True:
        lines = next_iter(lines)
        lines_as_string = ''.join(lines)
        if lines_as_string in seen:
            return sum(2**i for i, cell in enumerate(lines_as_string) if cell == '#')
        seen.add(lines_as_string)

def next_iter(lines):
    new_lines = []
    for y, row in enumerate(lines):
        new_line = ''
        for x, cell in enumerate(row):
            if cell == '#':
                if bugs_adjacent(lines, y, x) == 1:
                    new_line += '#'
                else:
                    new_line += '.'
            else:
                if bugs_adjacent(lines, y, x) in (1, 2):
                    new_line += '#'
                else:
                    new_line += '.'
        new_lines.append(new_line)
    return new_lines

def bugs_adjacent(lines, y, x):
    adj = ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
    s = 0
    for i, j in adj:
        if 0 <= i < len(lines[0]) and 0 <= j < len(lines):
            if lines[j][i] == '#':
                s += 1
    return s

def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        lines = [line.rstrip() for line in f.readlines()]
    grid = {}
    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            if (x, y) != (2, 2):
                grid[(x, y, 0)] = cell
    for _ in range(200):
        grid = next_iter_2(grid)
    return sum(1 for k, v in grid.items() if v == '#')

def next_iter_2(grid):
    max_z = max(grid.keys(), key=lambda p:p[2])[2]
    min_z = min(grid.keys(), key=lambda p:p[2])[2]
    needs_outer = False
    needs_inner = False
    for k, v in grid.items():
        if v == '#':
            if max_z == k[2]:
                needs_inner = True
            if min_z == k[2]:
                needs_outer = True
    if needs_inner:
        for x in range(5):
            for y in range(5):
                if (x, y) != (2, 2):
                    grid[(x, y, max_z + 1)] = '.'
    if needs_outer:
        for x in range(5):
            for y in range(5):
                if (x, y) != (2, 2):
                    grid[(x, y, min_z - 1)] = '.'
    new_grid = grid.copy()
    for point, cell in grid.items():
        bugs_adj = sum(1 for adj in adjacent(point) if
                       adj in grid and grid[adj] == '#')
        if cell == '#':
            if bugs_adj == 1:
                new_grid[point] = '#'
            else:
                new_grid[point] = '.'
        else:
            if bugs_adj in (1, 2):
                new_grid[point] = '#'
            else:
                new_grid[point] = '.'
    return new_grid
        

def adjacent(point):
    x, y, z = point
    if y == 0:
        up = [(2, 1, z - 1)]
    elif y == 3 and x == 2:
        up = [(n, 4, z + 1) for n in range(5)]
    else:
        up = [(x, y - 1, z)]
    if y == 4:
        down = [(2, 3, z - 1)]
    elif y == 1 and x == 2:
        down = [(n, 0, z + 1) for n in range(5)]
    else:
        down = [(x, y + 1, z)]
    if x == 0:
        left = [(1, 2, z - 1)]
    elif x == 3 and y == 2:
        left = [(4, n, z + 1) for n in range(5)]
    else:
        left = [(x - 1, y, z)]
    if x == 4:
        right = [(3, 2, z - 1)]
    elif x == 1 and y == 2:
        right = [(0, n, z + 1) for n in range(5)]
    else:
        right = [(x + 1, y, z)]
    return up + down + left + right

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
