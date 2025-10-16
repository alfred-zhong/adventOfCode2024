import sys, os
import itertools
from typing import List
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'common')))

from util import select_input_file

class Position():
    def __init__(self, val, x, y):
        self.val = val
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.val == other.val and self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.val, self.x, self.y))

    def __str__(self):
        return f'(val: {self.val}, x: {self.x}, y: {self.y})'

    def __repr__(self):
        return self.__str__()


class Map():
    def __init__(self, lines):
        self.matrix = []
        for line in lines:
            # print([int(x) for x in line.strip()])
            self.matrix.append([int(x) for x in line.strip()])

    def find_starts(self) -> List[Position]:
        starts = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    starts.append(Position(0, i, j))
        return starts
    
    def is_position_valid(self, pos: Position) -> bool:
        return pos.x >= 0 and pos.x < len(self.matrix) and pos.y >= 0 and pos.y < len(self.matrix[pos.x])
    
    def next_positions(self, pos: Position) -> List[Position]:
        left = Position(pos.val + 1, pos.x, pos.y - 1)
        right = Position(pos.val + 1, pos.x, pos.y + 1)
        up = Position(pos.val + 1, pos.x - 1, pos.y)
        down = Position(pos.val + 1, pos.x + 1, pos.y)

        # print(f'left: {left}, right: {right}, up: {up}, down: {down}')
        
        nexts = []
        if self.is_position_valid(left) and self.matrix[left.x][left.y] == left.val:
            nexts.append(left)
        if self.is_position_valid(right) and self.matrix[right.x][right.y] == right.val:
            nexts.append(right)
        if self.is_position_valid(up) and self.matrix[up.x][up.y] == up.val:
            nexts.append(up)
        if self.is_position_valid(down) and self.matrix[down.x][down.y] == down.val:
            nexts.append(down)
        return nexts

    
    def find_routes(self, start: Position) -> List[List[Position]]:
        routes = []
        
        temp = [[start]]
        while len(temp) > 0:
            new_temp = []
            for t in temp:
                last = t[len(t) - 1]
                nexts = self.next_positions(last)
                # print(f'last: {last}, nexts: {nexts}')
                for n in nexts:
                    if n.val == 9:
                        routes.append(t + [n])
                    else:
                        new_temp.append(t + [n])
            temp = new_temp
        
        return routes



with open(select_input_file(['example1.txt', 'example2.txt', 'input.txt'])) as f:
    map = Map(f.readlines())

# print(map.matrix)
starts = map.find_starts()
# print(starts)

score = 0
for start in starts:
    routes = map.find_routes(start)
    score += len(routes)
    # print(f'routes length: {len(routes)}')
print(f'score: {score}')
