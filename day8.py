DEFAULT_INPUT = 'day8.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        ints = f.readline().rstrip()
    layers = list(zip(*[iter(ints)]*150))
    layers.sort(key=lambda s:s.count('0'))
    return layers[0].count('1') * layers[0].count('2')
        
def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        ints = f.readline().rstrip()
    layers = list(zip(*[iter(ints)]*150))
    layered = ''
    for i in range(150):
        for layer in layers:
            if layer[i] == '1':
                layered += layer[i]
                break
            if layer[i] == '0':
                layered += ' '
                break
    layered = list(zip(*[iter(layered)]*25))
    print('\n'.join(''.join(layer) for layer in layered))
        
    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    part_2()
