from itertools import permutations
from intcode import IntCode

DEFAULT_INPUT = 'day7.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        memory = list(map(int, f.readline().rstrip().split(',')))
    perms = permutations(range(5))
    max_val = -1
    for perm in perms:
        a, b, c, d, e = perm
        a_res = IntCode(memory, a, 0).run_through()[0]
        b_res = IntCode(memory, b, a_res).run_through()[0]
        c_res = IntCode(memory, c, b_res).run_through()[0]
        d_res = IntCode(memory, d, c_res).run_through()[0]
        e_res = IntCode(memory, e, d_res).run_through()[0]
        largest = max(a_res, b_res, c_res, d_res, e_res)
        max_val = max(max_val, largest)
    return max_val
        
def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        memory = list(map(int, f.readline().rstrip().split(',')))
    perms = permutations(range(5, 10))
    max_val = -1
    for perm in perms:
        a, b, c, d, e = perm
        a_comp = IntCode(memory, a)
        b_comp = IntCode(memory, b)
        c_comp = IntCode(memory, c)
        d_comp = IntCode(memory, d)
        e_comp = IntCode(memory, e)
        finished = False
        prev_e_res = 0
        while not finished:
            a_comp.add_inputs(prev_e_res)
            a_res = a_comp.get_output()
            b_comp.add_inputs(a_res[1])
            b_res = b_comp.get_output()
            c_comp.add_inputs(b_res[1])
            c_res = c_comp.get_output()
            d_comp.add_inputs(c_res[1])
            d_res = d_comp.get_output()
            e_comp.add_inputs(d_res[1])
            e_res = e_comp.get_output()
            if e_res[0]:
                finished = True
                max_val = max(max_val, prev_e_res)
            else:
                prev_e_res = e_res[1]
    return max_val
        
        
    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
