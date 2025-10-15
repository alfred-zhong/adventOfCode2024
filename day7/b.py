
from enum import Enum
from itertools import product


class Op(Enum):
    ADD = 1
    MUL = 2
    COMBINE = 3

    def __str__(self):
        if self == Op.ADD:
            return '+'
        elif self == Op.MUL:
            return '*'
        else:
            return '||'
    
    def __repr__(self):
        return str(self)

class Equation():
    def __init__(self, line: str):
        ss = line.strip().split(':')
        self.result = int(ss[0])
        self.nums = [int(x) for x in ss[1].split()]
    
    def is_valid(self) -> bool:
        for ops in product([Op.ADD, Op.MUL, Op.COMBINE], repeat=len(self.nums)-1):
            res = self.nums[0]
            for i in range(len(ops)):
                if ops[i] == Op.ADD:
                    res += self.nums[i+1]
                    if res > self.result:
                        break
                elif ops[i] == Op.MUL:
                    res *= self.nums[i+1]
                    if res > self.result:
                        break
                else:
                    res = append(res, self.nums[i+1])
                    if res > self.result:
                        break
            if res == self.result:
                print(f'count: {len(ops)}, {ops}')
                return True
        return False

def append(x, y) -> int:
    r = y
    while r > 0:
        x *= 10
        r //=10
    return x + y

# print(append(12, 234))

with open(input("filename: ")) as f:
    equations = [Equation(line) for line in f.readlines()]

sum = 0
for eq in equations:
    if eq.is_valid():
        sum += eq.result
print(sum)
