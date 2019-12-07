from itertools import permutations
from intcode import IntCode

DEFAULT_INPUT = 'day7.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        instructions = list(map(int, f.readline().rstrip().split(',')))
    perms = permutations(range(5))
    max_val = -1
    for perm in perms:
        a, b, c, d, e = perm
        a_res = IntCode(instructions, a, 0).run_through()[0]
        b_res = IntCode(instructions, b, a_res).run_through()[0]
        c_res = IntCode(instructions, c, b_res).run_through()[0]
        d_res = IntCode(instructions, d, c_res).run_through()[0]
        e_res = IntCode(instructions, e, d_res).run_through()[0]
        largest = max(a_res, b_res, c_res, d_res, e_res)
        max_val = max(max_val, largest)
    return max_val
        
def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        instructions = list(map(int, f.readline().rstrip().split(',')))
    perms = permutations(range(5, 10))
    max_val = -1
    for perm in perms:
        a, b, c, d, e = perm
        a_comp = IntCode(instructions, a)
        b_comp = IntCode(instructions, b)
        c_comp = IntCode(instructions, c)
        d_comp = IntCode(instructions, d)
        e_comp = IntCode(instructions, e)
        finished = False
        prev_e_res = 0
        while not finished:
            a_comp.set_input(prev_e_res)
            a_res = a_comp.get_output()
            b_comp.set_input(a_res)
            b_res = b_comp.get_output()
            c_comp.set_input(b_res)
            c_res = c_comp.get_output()
            d_comp.set_input(c_res)
            d_res = d_comp.get_output()
            e_comp.set_input(d_res)
            e_res = e_comp.get_output()
            if e_res is True:
                finished = True
                max_val = max(max_val, prev_e_res)
            else:
                prev_e_res = e_res
    return max_val
        
        
    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
