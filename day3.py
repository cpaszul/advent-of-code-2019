from collections import defaultdict

DEFAULT_INPUT = 'day3.txt'

def day_3(loc=DEFAULT_INPUT):
    with open(loc) as f:
        wire_a = f.readline().rstrip().split(',')
        wire_b = f.readline().rstrip().split(',')
    points = defaultdict(set)
    steps_a = {}
    x,y = 0,0
    i = 1
    for move in wire_a:
        d, length = move[0], int(move[1:])
        if d == 'U':
            for _ in range(length):
                y += 1
                points[x].add(y)
                steps_a[(x, y)] = i
                i += 1
        elif d == 'D':
            for _ in range(length):
                y -= 1
                points[x].add(y)
                steps_a[(x, y)] = i
                i += 1
        elif d == 'R':
            for _ in range(length):
                x += 1
                points[x].add(y)
                steps_a[(x, y)] = i
                i += 1
        else:
            for _ in range(length):
                x -= 1
                points[x].add(y)
                steps_a[(x, y)] = i
                i += 1
    intersections = set()
    x, y = 0, 0
    steps_b = {}
    i = 1
    for move in wire_b:
        d, length = move[0], int(move[1:])
        if d == 'U':
            for _ in range(length):
                y += 1
                if y in points[x]:
                    intersections.add((x, y, steps_a[(x, y)], i))
                i += 1
        elif d == 'D':
            for _ in range(length):
                y -= 1
                if y in points[x]:
                    intersections.add((x, y, steps_a[(x, y)], i))
                i += 1
        elif d == 'R':
            for _ in range(length):
                x += 1
                if y in points[x]:
                    intersections.add((x, y, steps_a[(x, y)], i))
                i += 1
        else:
            for _ in range(length):
                x -= 1
                if y in points[x]:
                    intersections.add((x, y, steps_a[(x, y)], i))
                i += 1
    closest_p1 = min(intersections, key=lambda p:abs(p[0]) + abs(p[1]))
    p1_res = abs(closest_p1[0]) + abs(closest_p1[1])
    closest_p2 = min(intersections, key=lambda p:p[2] + p[3])
    p2_res = closest_p2[2] + closest_p2[3]
    return p1_res, p2_res
    
if __name__ == '__main__':
    res = day_3()
    print(f'Solution for Part One: {res[0]}\nSolution for Part Two: {res[1]}')
