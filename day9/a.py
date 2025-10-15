import sys, os
import itertools
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'common')))

from util import select_input_file

def is_num(s: str) -> bool:
    return s != '.'

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
                self.map.extend(itertools.repeat(str(index), int(s)))
                index += 1
            else:
                self.map.extend(itertools.repeat('.', int(s)))
            file = not file
        
        for i, v in enumerate(self.map):
            if not is_num(v):
                self.head = i
                break
        for i in range(len(self.map) - 1, -1, -1):
            if is_num(self.map[i]):
                self.tail = i
                break

    def forward_head(self):
        while self.head < len(self.map):
            self.head += 1
            if self.head >= len(self.map) or not is_num(self.map[self.head]):
                break
    
    def forward_tail(self):
        while self.tail >= 0:
            self.tail -= 1
            if self.tail < 0 or is_num(self.map[self.tail]):
                break
    
    def trim(self):
        while self.head < self.tail:
            self.map[self.head], self.map[self.tail] = self.map[self.tail], self.map[self.head]
            self.forward_head()
            self.forward_tail()
            
    @property
    def checksum(self):
        checksum = 0
        for i, v in enumerate(self.map):
            if not is_num(v):
                break
            checksum += i * int(v)
        return checksum
            

with open(select_input_file(['example.txt', 'example1.txt', 'input.txt'])) as f:
    disk = Disk(f.readline())

# print(disk.map)
print(''.join(disk.map))
print(f'length: {len(disk.map)}')
print(f'head: {disk.head}, tail: {disk.tail}')

disk.trim()

'''
print(''.join(disk.map))
print(f'length: {len(disk.map)}')
print(f'head: {disk.head}, tail: {disk.tail}')
'''

print(disk.checksum)
