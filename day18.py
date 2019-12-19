from collections import defaultdict, deque
from itertools import combinations
from heapq import heapify, heappop, heappush

DEFAULT_INPUT = 'day18.txt'
DEFAULT_INPUT_PART_2 = 'day18part2.txt'

def part_1(loc=DEFAULT_INPUT):
    grid = {}
    nodes = {}
    with open(loc) as f:
        lines = [line.rstrip() for line in f.readlines()]
    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            if cell.isalpha() and cell.islower():
                nodes[cell] = (x, y)
            grid[(x, y)] = cell
    return time_per_grid(grid, nodes)

def find_edges(grid, start):
    edges = {}
    d = deque([(start, 0, set())])
    seen = set([start])
    while d:
        cell, dist, doors = d.popleft()
        for adj in adjacent(cell):
            if adj not in grid or adj in seen or grid[adj] == '#':
                continue
            if grid[adj].islower():
                edges[grid[adj]] = dist + 1, doors
                continue
            new_doors = doors.copy()
            if grid[adj].isupper():
                new_doors.add(grid[adj].lower())
            seen.add(adj)
            d.append((adj, dist + 1, new_doors))
    return edges
        
def adjacent(cell):
    x, y = cell
    return [(x + 1, y), (x - 1, y),
            (x, y + 1), (x, y - 1)]    

def part_2(loc=DEFAULT_INPUT_PART_2):
    grid = {}
    nodes = {}
    with open(loc) as f:
        lines = [line.rstrip() for line in f.readlines()]
    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            if cell.isalpha() and cell.islower():
                nodes[cell] = (x, y)
            grid[(x, y)] = cell
    center_point = len(lines)//2
    upper_left = {k:v for k,v in grid.items()
                  if k[0] <= center_point and k[1] <= center_point}
    upper_right = {k:v for k,v in grid.items()
                  if k[0] >= center_point and k[1] <= center_point}
    lower_left = {k:v for k,v in grid.items()
                  if k[0] <= center_point and k[1] >= center_point}
    lower_right = {k:v for k,v in grid.items()
                  if k[0] >= center_point and k[1] >= center_point}
    grids = (upper_left, upper_right, lower_left, lower_right)
    return sum(time_per_grid(grid, nodes) for grid in grids)

def time_per_grid(grid, nodes):
    nodes = nodes.copy()
    keys = {n: nodes[n] for n in nodes if nodes[n] in grid}
    for coord, cell in grid.items():
        if cell.isupper() and cell.lower() not in keys:
            grid[coord] = '.'
        if cell == '@':
            nodes['@'] = coord
    dists = {node: find_edges(grid, nodes[node]) for node in nodes}
    h = []
    heappush(h, (0, '@', frozenset()))
    shortest = {}
    while h:
        dist, node, keys_obtained = heappop(h)
        if len(keys_obtained) == len(keys):
            return dist
        edges = dists[node]
        for edge_node, edge in edges.items():
            edge_len, doors = edge
            new_keys = keys_obtained
            new_dist = dist + edge_len
            if edge_node.islower():
                if not doors.issubset(new_keys):
                    continue
                new_keys |= frozenset(edge_node)
            if (edge_node, new_keys) not in shortest:
                shortest[(edge_node, new_keys)] = new_dist
            if new_dist > shortest[(edge_node, new_keys)]:
                continue
            shortest[(edge_node, new_keys)] = new_dist
            heappush(h, (new_dist, edge_node, new_keys))

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
