from enum import Enum
import sys, os
import itertools
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'common')))

from util import select_input_file

def is_num(s: str) -> bool:
    return s != '.'


class Block():
    def __init__(self, id, length):
        self.id = id
        self.length = length
    
    def is_file(self):
        return self.id >= 0
    
    def is_empty(self):
        return self.id < 0
    
    def __str__(self):
        return f'({self.id}, {self.length})'

    def __repr__(self):
        return f'({self.id}, {self.length})'
        


class Disk():
    def __init__(self, line):
        self.line = line.strip()
        self.extend()
    
    def extend(self):
        file = True
        index = 0
        self.map = []
        for s in self.line:
            if file:
                if int(s) > 0:
                    self.map.append(Block(index, int(s)))
                index += 1
            else:
                if int(s) > 0:
                    self.map.append(Block(-1, int(s)))
            file = not file
        
        for i in range(len(self.map) - 1, -1, -1):
            if self.map[i].is_file():
                self.tail = i
                break
    
    def forward_tail(self):
        while self.tail >= 0:
            self.tail -= 1
            if self.tail < 0 or self.map[self.tail].is_file():
                print(self.tail)
                break
    
    def trim(self):
        while self.tail >= 0:
            l = self.map[self.tail].length
            for i in range(self.tail):
                if self.map[i].is_empty() and self.map[i].length >= l:
                    if self.map[i].length == l:
                        self.map[i], self.map[self.tail] = self.map[self.tail], self.map[i]
                    else:
                        self.map = self.map[:i] + [self.map[self.tail]] + [Block(-1, self.map[i].length - l)] + self.map[i+1:self.tail] + [Block(-1, l)] + self.map[self.tail+1:]
                        self.tail += 1
                    # self.print()
                    break

            self.forward_tail()
    
    def transform(self):
        s = []
        for v in self.map:
            if v.is_file():
                s.extend(itertools.repeat(str(v.id), v.length))
            else:
                s.extend(itertools.repeat('.', v.length))
        return s

    def print(self):
        print(''.join(self.transform()))

    @property
    def checksum(self):
        s = self.transform()
        checksum = 0
        for i, v in enumerate(s):
            if is_num(v):
                checksum += i * int(v)
        return checksum
            

with open(select_input_file(['example.txt', 'example1.txt', 'input.txt'])) as f:
    disk = Disk(f.readline())

# disk.print()
# print(f'length: {len(disk.map)}')
# print(f'head: {disk.head}, tail: {disk.tail}')

disk.trim()

# disk.print()
'''
print(''.join(disk.map))
print(f'length: {len(disk.map)}')
print(f'head: {disk.head}, tail: {disk.tail}')
'''

print(disk.checksum)
