DEFAULT_INPUT = '372304-847060'

def day_4(password_range=DEFAULT_INPUT):
    start, end = map(int, password_range.split('-'))
    p1, p2 = 0, 0
    for ps in range(start, end + 1):
        res_1, res_2 = is_valid(ps)
        if res_1:
            p1 += 1
        if res_2:
            p2 += 1
    return p1, p2

def is_valid(n):
    s = str(n)
    pairs = set()
    triples = set()
    for a, b, c in zip(s, s[1:], s[2:]):
        if a > b or b > c:
            return False, False
        if a == b:
            pairs.add(a)
        if b == c:
            pairs.add(b)
        if a == b == c:
            triples.add(a)
    return len(pairs) > 0, len(pairs) > len(triples)
    
if __name__ == '__main__':
    res = day_4()
    print(f'Solution for Part One: {res[0]}\nSolution for Part Two: {res[1]}')
