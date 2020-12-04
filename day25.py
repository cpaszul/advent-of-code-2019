from intcode import IntCode
import itertools

DEFAULT_INPUT = 'day25.txt'

class Game:
    valid = ('candy cane', 'mutex', 'boulder', 'loom',
             'mug', 'prime number', 'food ration', 'asterisk')
    
    def __init__(self, comp):
        self.comp = comp
        print(self.comp.run_until_command())

    def command(self, text):
        self.comp.add_ascii_inputs(text)
        return self.comp.run_until_command()

    def take(self, text):
        print(self.command(f'take {text}'))

    @property
    def inv(self):
        print(self.command('inv'))

    def drop(self, text):
        print(self.command(f'drop {text}'))

    @property
    def north(self):
        print(self.command('north'))
        
    @property
    def west(self):
        print(self.command('west'))
        
    @property
    def east(self):
        print(self.command('east'))
        
    @property
    def south(self):
        print(self.command('south'))

    def get_inv(self):
        text = self.command('inv')
        items = [line[2:].rstrip() for line in text.split('\n')
                 if line[:2] == '- ']
        return items

    def solve(self):
        def powerset(iterable):
            s = list(iterable)
            return itertools.chain.from_iterable(itertools.combinations(s, r)
                                                 for r in range(len(s)+1))
        for item_set in powerset(self.valid):
            current_inv = self.get_inv()
            for item in current_inv:
                if item not in item_set:
                    self.command(f'drop {item}')
            for item in item_set:
                if item not in current_inv:
                    self.command(f'take {item}')
            attempt = self.command('north')
            if 'Alert!' not in attempt:
                return int(attempt.split('typing ')[1].split(' on')[0])
            
    moves = ('south', 'take boulder', 'east', 'take food ration', 'west',
             'west', 'take asterisk', 'east', 'north', 'east',
             'take candy cane', 'north', 'north', 'take mutex', 'north',
             'take prime number', 'south', 'south', 'east', 'north',
             'take mug', 'south', 'west', 'south', 'east', 'north',
             'take loom', 'south', 'east', 'south', 'east', 'east')

    def to_puzzle_start(self):
        for move in self.moves:
            self.command(move)
        

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        memory = list(map(int, f.readline().rstrip().split(',')))
    comp = IntCode(memory)
    g = Game(comp)
    g.to_puzzle_start()
    return g.solve()

if __name__ == '__main__':
    print('Solution for Part One:', part_1())

'''

    E-F
    |
  G-D I
    | |
    C-H
    |
    | K
    | |
  A-B-J-L   *
  |     |   |
S-Q-R P-M-N-O



A - hull breach
B - crew quarters, candy cane
C - stables, infinite loop !DO NOT TAKE!
D - hallway, mutex
E - hot choc fount, prime number
F - corridor, escape pod !DO NOT TAKE!
G - arcade, giant electromagnet !DO NOT TAKE!
H - engineering
I - navigation, mug
J - kitchen
K - storage, loom
L - warp drive maintenance
M - passages
N - sick bay, photons !DO NOT TAKE!
O - security checkpoint
P - gift wrapping center, molten lava !DO NOT TAKE!
Q - holodeck, boulder
R - science lab, food ration
S - observatory, asterisk

8 items:
candy cane
mutex
prime number
mug
loom
boulder
food ration
asterisk
'''
