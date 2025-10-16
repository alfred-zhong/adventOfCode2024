import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'common')))

from util import select_input_file
from typing import Tuple

class Formula():
    def __init__(self, x1, x2, x3, y1, y2, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3

    def __str__(self):
        return f'{self.x1}a + {self.x2}b = {self.x3}, {self.y1}a + {self.y2}b = {self.y3}'
    
    def __repr__(self):
        return self.__str__()
    
    def solve(self) -> Tuple[bool, int, int]:
        a_d = (self.x2 * self.y3 - self.x3 * self.y2) % (self.x2 * self.y1 - self.x1 * self.y2)
        b_d = (self.x1 * self.y3 - self.x3 * self.y1) % (self.x1 * self.y2 - self.x2 * self.y1)

        if a_d != 0 or b_d != 0:
            return False, 0, 0
        
        return True, (self.x2 * self.y3 - self.x3 * self.y2) // (self.x2 * self.y1 - self.x1 * self.y2), (self.x1 * self.y3 - self.x3 * self.y1) // (self.x1 * self.y2 - self.x2 * self.y1)

with open(select_input_file(['example.txt', 'input.txt'])) as f:
    formulas = []
    lines = f.readlines()
    for i in range(0, len(lines), 4):
        x1, y1 = [int(s.split('+')[1]) for s in lines[i].split(':')[1].split(',')]
        x2, y2 = [int(s.split('+')[1]) for s in lines[i+1].split(':')[1].split(',')]
        x3, y3 = [int(s.split('=')[1]) for s in lines[i+2].split(':')[1].split(',')]
        formulas.append(Formula(x1, x2, x3, y1, y2, y3))

costs = 0
for formula in formulas:
    solve, a, b = formula.solve()
    if solve:
        print(f'{formula}, a = {a}, b = {b}')
        costs += 3 * a + b
print(f'costs = {costs}')
    
