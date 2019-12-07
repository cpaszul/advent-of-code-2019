from collections import defaultdict, deque

DEFAULT_INPUT = 'day6.txt'

def part_1(loc=DEFAULT_INPUT):
    orbits = {}
    with open(loc) as f:
        for line in f.readlines():
            inner, outer = line.rstrip().split(')')
            orbits[outer] = inner
    all_orbits = sum(num_orbits(orbits, obj) for obj in orbits)
    return all_orbits

def num_orbits(orbits, obj):
    if obj not in orbits:
        return 0
    return 1 + num_orbits(orbits, orbits[obj])
        
def part_2(loc=DEFAULT_INPUT):
    orbits = defaultdict(set)
    with open(loc) as f:
        for line in f.readlines():
            inner, outer = line.rstrip().split(')')
            orbits[outer].add(inner)
            orbits[inner].add(outer)
    d = deque([('YOU', -1)])
    seen = set(['YOU'])
    while d:
        current_obj, transfers = d.popleft()
        for obj in orbits[current_obj]:
            if obj == 'SAN':
                return transfers
            if obj not in seen:
                seen.add(obj)
                d.append((obj, transfers + 1))
    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
