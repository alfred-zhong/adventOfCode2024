from enum import Enum
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'common')))

from util import select_input_file


class Dir(Enum):
    UP = '^'
    DOWN = 'v'
    LEFT = '<'
    RIGHT = '>'


class Map():
    def __init__(self, lines):
        self.matrix = []
        for line in lines:
            self.matrix.append([x for x in line.strip()])
        # find robot
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                if self.matrix[x][y] == '@':
                    self.robot = (x, y)
        
    def print(self):
        for line in self.matrix:
            print(''.join(line))
        print()
    
    def contains(self, x, y):
        return 0 <= x < len(self.matrix) and 0 <= y < len(self.matrix[x])
    
    def __move(self, x, y, dir: Dir):
        val = self.matrix[x][y]
        new_x, new_y = x, y
        if dir == Dir.UP:
            new_x -= 1
        elif dir == Dir.DOWN:
            new_x += 1
        elif dir == Dir.LEFT:
            new_y -= 1
        elif dir == Dir.RIGHT:
            new_y += 1
        # can't move
        if not self.contains(new_x, new_y):
            return
        # wall, can't move
        if self.matrix[new_x][new_y] == '#':
            return
        # box, move it
        if self.matrix[new_x][new_y] == 'O':
            self.__move(new_x, new_y, dir)
        
        if self.matrix[new_x][new_y] == '.':
            self.matrix[new_x][new_y] = val
            self.matrix[x][y] = '.'
            if val == '@':
                self.robot = (new_x, new_y)
        

    def move(self, dir: Dir):
        self.__move(self.robot[0], self.robot[1], dir)

    def __box_score(self, x, y) -> int:
        # up
        up_score = x
        # left
        left_score = y
        return 100 * up_score + left_score
    
    def box_score(self) -> int:
        score = 0
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                if self.matrix[x][y] == 'O':
                    score += self.__box_score(x, y)
        return score
        


with open(select_input_file(['example1.txt', 'example2.txt','input.txt'])) as f:
    map_zone = True
    map_lines = []
    moves = []

    line = f.readline()
    while line:
        if line.strip() == '':
            map_zone = False
        elif map_zone:
            map_lines.append(line.strip())
        else:
            for s in line.strip():
                moves.append(Dir(s))
        line = f.readline()
    map = Map(map_lines)
    
# map.print()

for move in moves:
    map.move(move)
    # print(f'Move {move.value}:')
    # map.print()

print(f'Box score: {map.box_score()}')
