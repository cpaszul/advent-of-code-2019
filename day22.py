import re

DEFAULT_INPUT = 'day22.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        instructions = [line.rstrip() for line in f.readlines()]
    deck = list(range(10007))
    cut = re.compile(r'cut (-?\d+)')
    deal = re.compile(r'deal with increment (\d+)')
    for inst in instructions:
        if m := cut.match(inst):
            n = int(m.group(1))
            deck = deck[n:] + deck[:n]
        elif m := deal.match(inst):
            n = int(m.group(1))
            new_deck = [0] * len(deck)
            i = 0
            for card in deck:
                new_deck[i] = card
                i = (i + n) % len(deck)
            deck = new_deck
        else:
            deck = deck[::-1]
    return deck.index(2019)

def part_2(loc=DEFAULT_INPUT):
    #Solution taken from:
    # https://www.reddit.com/r/adventofcode/comments/ee0rqi/2019_day_22_solutions/fbqs5bk/?st=k4hfgrn9&sh=88587f8f
    with open(loc) as f:
        instructions = [line.rstrip() for line in f.readlines()]
    cut = re.compile(r'cut (-?\d+)')
    deal = re.compile(r'deal with increment (\d+)')
    mod = 119315717514047
    iters = 101741582076661
    inv = lambda x: pow(x, mod - 2, mod)
    off = 0
    inc = 1
    for inst in instructions:
        if m := cut.match(inst):
            n = int(m.group(1))
            off += inc * n
        elif m := deal.match(inst):
            n = int(m.group(1))
            inc *= inv(n)
        else:
            off -= inc
            inc *= -1
    off *= inv(1 - inc)
    inc = pow(inc, iters, mod)
    return (2020 * inc + (1 - inc) * off) % mod

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
