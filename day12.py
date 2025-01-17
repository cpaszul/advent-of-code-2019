import re
from itertools import combinations
from math import gcd
from functools import reduce

DEFAULT_INPUT = 'day12.txt'

class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.vy = 0
        self.vz = 0

    def apply_gravity(self, other):
        if other.x > self.x:
            self.vx += 1
        if other.x < self.x:
            self.vx -= 1
        if other.y > self.y:
            self.vy += 1
        if other.y < self.y:
            self.vy -= 1
        if other.z > self.z:
            self.vz += 1
        if other.z < self.z:
            self.vz -= 1

    def apply_velocity(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def total_energy(self):
        return (abs(self.x) + abs(self.y) + abs(self.z)) * \
               (abs(self.vx) + abs(self.vy) + abs(self.vz))

def part_1(loc=DEFAULT_INPUT):
    moon_re = re.compile(r'-?\d+')
    with open(loc) as f:
        lines = [line for line in f.readlines()]
    moons = [Moon(*map(int, moon_re.findall(line))) for line in lines]
    for _ in range(1000):
        increment(moons)
    return sum(moon.total_energy() for moon in moons)

def increment(moons):
    for moon_a, moon_b in combinations(moons, 2):
        moon_a.apply_gravity(moon_b)
        moon_b.apply_gravity(moon_a)
    for moon in moons:
        moon.apply_velocity()
    
def part_2(loc=DEFAULT_INPUT):
    moon_re = re.compile(r'-?\d+')
    with open(loc) as f:
        lines = [line for line in f.readlines()]
    moons = [Moon(*map(int, moon_re.findall(line))) for line in lines]
    initial_x = tuple((moon.x, moon.vx) for moon in moons)
    initial_y = tuple((moon.y, moon.vy) for moon in moons)
    initial_z = tuple((moon.z, moon.vz) for moon in moons)
    i = 1
    x_repeat = y_repeat = z_repeat = False
    while not (x_repeat and y_repeat and z_repeat):
        increment(moons)
        if not x_repeat:
            x_state = tuple((moon.x, moon.vx) for moon in moons)
            if x_state == initial_x:
                x_period = i
                x_repeat = True
        if not y_repeat:
            y_state = tuple((moon.y, moon.vy) for moon in moons)
            if y_state == initial_y:
                y_period = i
                y_repeat = True
        if not z_repeat:
            z_state = tuple((moon.z, moon.vz) for moon in moons)
            if z_state == initial_z:
                z_period = i
                z_repeat = True
        i += 1
    return lcm(x_period, y_period, z_period)

def lcm(*nums):
    return reduce(lambda x, y: (x * y) // gcd(x, y), nums, 1)
        
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
