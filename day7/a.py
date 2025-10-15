
from enum import Enum
from itertools import product


class Op(Enum):
    ADD = 1
    MUL = 2

class Equation():
    def __init__(self, line: str):
        ss = line.strip().split(':')
        self.result = int(ss[0])
        self.nums = [int(x) for x in ss[1].split()]
    
    def is_valid(self) -> bool:
        for ops in product([Op.ADD, Op.MUL], repeat=len(self.nums)-1):
            res = self.nums[0]
            for i in range(len(ops)):
                if ops[i] == Op.ADD:
                    res += self.nums[i+1]
                else:
                    res *= self.nums[i+1]
            if res == self.result:
                return True
        return False

with open(input("filename: ")) as f:
    equations = [Equation(line) for line in f.readlines()]

sum = 0
for eq in equations:
    if eq.is_valid():
        sum += eq.result
print(sum)
