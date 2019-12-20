from collections import defaultdict, deque

DEFAULT_INPUT = 'day20.txt'

def part_1(loc=DEFAULT_INPUT):
    graph = defaultdict(set)
    open_cells = set()
    portals = {}
    portal_names = set()
    with open(loc) as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            if cell == '.':
                open_cells.add((x, y))
    for y_a in range(len(lines) - 1):
        y_b = y_a + 1
        row_a = lines[y_a]
        row_b = lines[y_b]
        for x, cell_a in enumerate(row_a):
            cell_b = row_b[x]
            if cell_a not in ' .#' and cell_b not in ' .#':
                portals[(x, y_a)] = cell_a + cell_b
                portals[(x, y_b)] = cell_a + cell_b
                portal_names.add(cell_a + cell_b)
    for y, row in enumerate(lines):
        for x_a in range(len(row) - 1):
            x_b = x_a + 1
            cell_a = row[x_a]
            cell_b = row[x_b]
            if cell_a not in ' .#' and cell_b not in ' .#':
                portals[(x_a, y)] = cell_a + cell_b
                portals[(x_b, y)] = cell_a + cell_b
                portal_names.add(cell_a + cell_b)
    for cell in open_cells:
        for adj in adjacent(cell):
            if adj in open_cells:
                graph[cell].add(adj)
                graph[adj].add(cell)
            if adj in portals:
                graph[cell].add(portals[adj])
                graph[portals[adj]].add(cell)
                if portals[adj] == 'AA':
                    start = cell
                if portals[adj] == 'ZZ':
                    end = cell
    for portal in portal_names:
        if portal not in ('AA', 'ZZ'):
            cell_a, cell_b = graph[portal]
            graph[cell_a].add(cell_b)
            graph[cell_a].remove(portal)
            graph[cell_b].add(cell_a)
            graph[cell_b].remove(portal)
    shortest = {start: 0}
    d = deque([(start, 0)])
    while d:
        cell, dist = d.popleft()
        for adj in graph[cell]:
            if adj == end:
                return dist + 1
            new_dist = dist + 1
            if adj not in shortest:
                shortest[adj] = new_dist
            if new_dist > shortest[adj]:
                continue
            d.append((adj, new_dist))

def adjacent(cell):
    x, y = cell
    return [(x + 1, y), (x - 1, y),
            (x, y + 1), (x, y - 1)]
    

def part_2(loc=DEFAULT_INPUT):
    graph = defaultdict(set)
    open_cells = set()
    portals = {}
    portal_names = set()
    with open(loc) as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
    max_x = len(lines[0])
    max_y = len(lines)
    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            if cell == '.':
                open_cells.add((x, y))
    for y_a in range(len(lines) - 1):
        y_b = y_a + 1
        row_a = lines[y_a]
        row_b = lines[y_b]
        for x, cell_a in enumerate(row_a):
            cell_b = row_b[x]
            if cell_a not in ' .#' and cell_b not in ' .#':
                portals[(x, y_a)] = cell_a + cell_b
                portals[(x, y_b)] = cell_a + cell_b
                portal_names.add(cell_a + cell_b)
    for y, row in enumerate(lines):
        for x_a in range(len(row) - 1):
            x_b = x_a + 1
            cell_a = row[x_a]
            cell_b = row[x_b]
            if cell_a not in ' .#' and cell_b not in ' .#':
                portals[(x_a, y)] = cell_a + cell_b
                portals[(x_b, y)] = cell_a + cell_b
                portal_names.add(cell_a + cell_b)
    for cell in open_cells:
        for adj in adjacent(cell):
            if adj in open_cells:
                graph[cell].add((adj, 0))
                graph[adj].add((cell, 0))
            if adj in portals:
                outer = is_outer(cell, adj, max_x, max_y)
                graph[cell].add(portals[adj])
                graph[portals[adj]].add((cell, 1 if outer else -1))
                if portals[adj] == 'AA':
                    start = cell
                    graph[cell].remove('AA')
                if portals[adj] == 'ZZ':
                    end = cell
                    graph[cell].remove('ZZ')
    for portal in portal_names:
        if portal not in ('AA', 'ZZ'):
            t_a, t_b = graph[portal]
            cell_a, shift_a = t_a
            cell_b, shift_b = t_b
            graph[cell_a].add((cell_b, shift_b))
            graph[cell_a].remove(portal)
            graph[cell_b].add((cell_a, shift_a))
            graph[cell_b].remove(portal)
    shortest = {(start, 0): 0}
    d = deque([(start, 0, 0)])
    while d:
        cell, depth, dist = d.popleft()
        for adj, shift in graph[cell]:
            new_dist = dist + 1
            new_depth = depth + shift
            if new_depth < 0:
                continue
            if adj == end and new_depth == 0:
                return new_dist
            if (adj, new_depth) not in shortest:
                shortest[(adj, new_depth)] = new_dist
            if new_dist > shortest[(adj, new_depth)]:
                continue
            d.append((adj, new_depth, new_dist))

def is_outer(cell, adj, max_x, max_y):
    horizontal = cell[1] == adj[1]
    if horizontal:
        left_half = adj[0] < max_x // 2
        if left_half:
            return adj[0] < cell[0]
        return adj[0] > cell[0]
    upper_half = adj[1] < max_y // 2
    if upper_half:
        return adj[1] < cell[1]
    return adj[1] > cell[1]

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
