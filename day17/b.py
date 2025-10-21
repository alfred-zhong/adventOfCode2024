from enum import Enum
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'common')))

from util import select_input_file

class Instruction(Enum):
    ADV = 0
    BXL = 1
    BST = 2
    JNZ = 3
    BXC = 4
    OUT = 5
    BDV = 6
    CDV = 7

class Unit():
    def __init__(self, a, b, c, program):
        self.a = a
        self.b = b
        self.c = c
        self.program = program
        self.i = 0
        self.out = []
    
    def __get_data(self, combo: int) -> int:
        if 0 <= combo <= 3:
            return combo
        elif combo == 4:
            return self.a
        elif combo == 5:
            return self.b
        elif combo == 6:
            return self.c
        return combo
    
    def run(self):
        while self.i < len(self.program):
            ins = Instruction(self.program[self.i])
            combo = self.program[self.i + 1]
            
            if ins == Instruction.ADV:
                self.a = self.a // (2 ** self.__get_data(combo))
            elif ins == Instruction.BXL:
                self.b = self.b ^ combo
            elif ins == Instruction.BST:
                self.b = self.__get_data(combo) % 8
            elif ins == Instruction.JNZ:
                if self.a != 0:
                    self.i = combo
                    continue
            elif ins == Instruction.BXC:
                self.b = self.b ^ self.c
            elif ins == Instruction.OUT:
                self.out.append(self.__get_data(combo) % 8)
            elif ins == Instruction.BDV:
                self.b = self.a // (2 ** self.__get_data(combo))
            elif ins == Instruction.CDV:
                self.c = self.a // (2 ** self.__get_data(combo))
            
            # print(f'a: {self.a}, b: {self.b}, c: {self.c}')
            self.i += 2
    
    @property
    def out_str(self) -> str:
        return ','.join(map(str, self.out))


    
with open(select_input_file(['example3.txt', 'input.txt'])) as f:
    a = int(f.readline().strip().split(":")[1])
    b = int(f.readline().strip().split(":")[1])
    c = int(f.readline().strip().split(":")[1])
    f.readline()
    program = [int(x) for x in f.readline().strip().split(":")[1].split(',')]

program_str = ','.join([str(x) for x in program])
print(f'program len: {len(program_str)}')

'''
a = int(1e20)
unit = Unit(a, b, c, program)
unit.run()
print(f'a = {a}, out: {unit.out_str}')

a = int(1e20) + 20000
unit = Unit(a, b, c, program)
unit.run()
print(f'a = {a}, out: {unit.out_str}')
'''

'''
a = int(1 << 48)
unit = Unit(a, b, c, program)
unit.run()
print(f'a = {a}, out len: {len(unit.out_str)}')

print((1 << 48) - (1 << 45))
'''

'''
start, end = 1, int(1e20)
while start <= end:
    print(f'start: {start}, end: {end}')
    mid = (start + end) // 2
    unit = Unit(mid, b, c, program)
    unit.run()
    if len(unit.out_str) == len(program_str):
        print(f'out: {unit.out_str}')
        if unit.out_str == program_str:
            print(f'a = {mid}, out: {unit.out_str}')
            break
        elif unit.out_str < program_str:
            start = mid
        else:
            end = mid
    elif len(unit.out_str) < len(program_str):
        start = mid
    else:
        end = mid
'''

candidates = [0]
for l in range(len(program)):
    print(candidates)
    next_candicates = []
    for c in candidates:
        for i in range(8):
            target = (c << 3) + i
            unit = Unit(target, b, c, program)
            unit.run()
            if unit.out == program[-l-1:]:
                next_candicates.append(target)
    candidates = next_candicates

print(min(candidates))
