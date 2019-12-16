from itertools import accumulate

DEFAULT_INPUT = 'day16.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        ar = list(map(int, list(f.readline().rstrip())))
    for _ in range(100):
        ar = fft(ar)
    return ''.join(map(str, ar[:8]))

def fft(ar):
    new_ar = []
    for pos in range(1, len(ar) + 1):
        pattern = [0,] * pos + [1,] * pos + [0,] * pos + [-1,] * pos
        ele_ar = []
        for ind, ele in enumerate(ar):
            pattern_ind = (ind + 1) % len(pattern)
            ele_ar.append(ele * pattern[pattern_ind])
        new_ar.append(abs(sum(ele_ar)) % 10)
    return new_ar

def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        ar = list(map(int, list(f.readline().rstrip()))) * 10000
    offset = int(''.join(map(str, ar[:7])))
    ar = ar[offset:][::-1]
    for _ in range(100):
        ar = list(accumulate(ar, lambda a,b:(a + b) % 10))
    ar = ar[::-1]
    return ''.join(map(str, ar[:8]))

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
