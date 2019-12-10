from collections import namedtuple, Counter
from itertools import combinations
import math


Point = namedtuple('Point', ['x', 'y'])
Asteroid = namedtuple('Asteroid', ['coord', 'angle', 'dist'])

DEFAULT_INPUT = 'day10.txt'

def day_10(loc=DEFAULT_INPUT):
    asteroids = []
    visible = Counter()
    with open(loc) as f:
        grid = [line.rstrip() for line in f.readlines()]
    max_x = len(grid[0])
    max_y = len(grid)
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '#':
                asteroids.append(Point(x, y))
    for point_a, point_b in combinations(asteroids, 2):
        if can_see(point_a, point_b, asteroids):
            visible[point_a] += 1
            visible[point_b] += 1
    station, p1_res = max(visible.items(), key=lambda p:p[1])
    all_asteroids = [Asteroid(point, angle(station, point), math.dist(station, point))
                     for point in asteroids if point != station]
    to_remove = all_asteroids.copy()
    removed = set()
    remove_num = 1
    while True:
        to_remove.sort(key=lambda a:a.dist)
        to_remove.sort(key=lambda a:a.angle)
        target = to_remove[0]
        if remove_num == 200:
            p2_res = target.coord.x * 100 + target.coord.y
            break
        removed.add(target.coord)
        remove_num += 1
        to_remove = [ast for ast in all_asteroids
                     if ast.coord not in removed and ast.angle > target.angle]
        if not to_remove:
            to_remove = [ast for ast in all_asteroids if ast.coord not in removed]
    return p1_res, p2_res

def can_see(start, end, other):
    for point in other:
        if point not in (start, end):
            if point_on_line(start, end, point):
                return False
    return True
            
def point_on_line(start, end, point):
    if ((start.x <= point.x <= end.x) or (start.x >= point.x >= end.x)) and \
       ((start.y <= point.y <= end.y) or (start.y >= point.y >= end.y)):
        cross_product = (end.x - start.x) * (point.y - start.y) - \
                        (end.y - start.y) * (point.x - start.x)
        return cross_product == 0
    return False

def angle(station, point):
    if point.x == station.x:
        if point.y < station.y:
            return 0
        return 180
    p2 = Point(station.x, station.y - 10)
    a = math.dist(station, p2)
    b = math.dist(station, point)
    c = math.dist(point, p2)
    C = round(math.degrees(math.acos((a**2 + b**2 - c**2)/(2*a*b))), 3)
    if point.x > station.x:
        return C
    return 360 - C
    
if __name__ == '__main__':
    res = day_10()
    print(f'Solution for Part One: {res[0]}\nSolution for Part Two: {res[1]}')
