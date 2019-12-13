from intcode import IntCode

DEFAULT_INPUT = 'day13.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        instructions = list(map(int, f.readline().rstrip().split(',')))
    ic = IntCode(instructions)
    outputs = ic.run_through()
    draw_instructions = list(zip(*[iter(outputs)]*3))
    return sum(1 for t in draw_instructions if t[2] == 2)
    
def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        instructions = list(map(int, f.readline().rstrip().split(',')))
    instructions[0] = 2
    ic = IntCode(instructions)
    score = -1
    paddle_x = 0
    while True:
        x = ic.get_output()
        y = ic.get_output()
        tile = ic.get_output()
        if x[0] or y[0] or tile[0]:
            return score
        if x[1] == -1 and y[1] == 0:
            score = tile[1]
        elif tile[1] == 3:
            paddle_x = x[1]
        elif tile[1] == 4:
            ball_x = x[1]
            if ball_x > paddle_x:
                ic.set_input(1)
            elif ball_x < paddle_x:
                ic.set_input(-1)
            else:
                ic.set_input(0)

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
