from collections import defaultdict
import re
from math import ceil

DEFAULT_INPUT = 'day14.txt'

def day_14(loc=DEFAULT_INPUT):
    with open(loc) as f:
        raw_reactions = [line.rstrip() for line in f.readlines()]
    reactions = {}
    reg = re.compile(r'\d+ \w+')
    for line in raw_reactions:
        components = reg.findall(line)
        inputs, output = components[:-1], components[-1]
        output_quantity, output_name = output.split(' ')
        output_quantity = int(output_quantity)
        inputs = {inp.split(' ')[1]: int(inp.split(' ')[0])
                  for inp in inputs}
        reactions[output_name] = (output_quantity, inputs)
    p1_res = ore_needed(reactions, 1)
    target = 1000000000000
    success = 1
    fail = 1000000000000
    while True:
        if success + 1 == fail:
            p2_res = success
            break
        guess = success + ((fail - success) // 2)
        guess_ore = ore_needed(reactions, guess)
        if guess_ore == target:
            p2_res = guess
            break
        elif guess_ore < target:
            success = guess
        else:
            fail = guess
    return p1_res, p2_res

def ore_needed(reactions, fuel_num):
    chems = defaultdict(int)
    chems['FUEL'] = fuel_num
    while True:
        required = [k for k,v in chems.items() if k != 'ORE' and v > 0]
        if not required:
            return chems['ORE']
        to_produce = required[0]
        quant_needed = chems[to_produce]
        quant_per_rx, chems_needed = reactions[to_produce]
        mult = ceil(quant_needed / quant_per_rx)
        quant_to_produce = quant_per_rx * mult
        for ch in chems_needed:
            chems[ch] += chems_needed[ch] * mult
        chems[to_produce] -= quant_to_produce

if __name__ == '__main__':
    res = day_14()
    print(f'Solution for Part One: {res[0]}\nSolution for Part Two: {res[1]}')
