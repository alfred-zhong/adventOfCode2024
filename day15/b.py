from hashlib import new
from enum import Enum
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'common')))

from util import select_input_file


class Dir(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, tuple):
            return Pos(self.x + other[0], self.y + other[1])
        elif isinstance(other, Pos):
            return Pos(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))


class Map():
    def __init__(self, lines):
        self.matrix = []
        for line in lines:
            self.matrix.append([x for x in line.strip()])
        # find robot
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                if self.matrix[x][y] == '@':
                    self.robot = Pos(x, y)
        
    def print(self):
        for line in self.matrix:
            print(''.join(line))
        print()
    
    def extend(self):
        new_matrix = []
        for line in self.matrix:
            new_line = []
            for s in line:
                if s == '#':
                    new_line.extend(['#', '#'])
                elif s == 'O':
                    new_line.extend(['[', ']'])
                elif s == '.':
                    new_line.extend(['.', '.'])
                elif s == '@':
                    new_line.extend(['@', '.'])
            new_matrix.append(new_line)
        self.matrix = new_matrix
        # find robot
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                if self.matrix[x][y] == '@':
                    self.robot = Pos(x, y)
                
    
    def contains(self, pos: Pos):
        return 0 <= pos.x < len(self.matrix) and 0 <= pos.y < len(self.matrix[pos.x])
    
    def __find_ref(self, refs, pos: Pos, dir: Dir):
        if self.matrix[pos.x][pos.y] == '@':
            refs.add(pos)

            self.__find_ref(refs, pos + dir.value, dir)
        elif self.matrix[pos.x][pos.y] == '[':
            refs.add(pos)
            refs.add(pos + (0, 1))

            self.__find_ref(refs, pos + dir.value, dir)
            if dir == Dir.UP or dir == Dir.DOWN:
                self.__find_ref(refs, pos + dir.value + (0, 1), dir)
        elif self.matrix[pos.x][pos.y] == ']':
            refs.add(pos)
            refs.add(pos + (0, -1))

            self.__find_ref(refs, pos + dir.value, dir)
            if dir == Dir.UP or dir == Dir.DOWN:
                self.__find_ref(refs, pos + dir.value + (0, -1), dir)

    def __can_move(self, refs, dir: Dir) -> bool:
        for pos in refs:
            next_pos = pos + dir.value
            if self.matrix[next_pos.x][next_pos.y] == '#':
                return False
        return True

    def __move(self, refs: set, dir: Dir):
        while len(refs) > 0:
            pos = refs.pop()
            val = self.matrix[pos.x][pos.y]

            next_pos = pos + dir.value
            if self.matrix[next_pos.x][next_pos.y] == '.':
                self.matrix[pos.x][pos.y] = '.'
                self.matrix[next_pos.x][next_pos.y] = val

                if val == '@':
                    self.robot = next_pos
            else:
                refs.add(pos)
            
    def move(self, dir: Dir):
        refs = set()
        self.__find_ref(refs, self.robot, dir)
        # print(f'Find refs: {refs}')
        if self.__can_move(refs, dir):
            self.__move(refs, dir)

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
                if self.matrix[x][y] == '[':
                    score += self.__box_score(x, y)
        return score
        


with open(select_input_file(['example3.txt', 'example2.txt','input.txt'])) as f:
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
                if s == '^':
                    moves.append(Dir.UP)
                elif s == 'v':
                    moves.append(Dir.DOWN)
                elif s == '<':
                    moves.append(Dir.LEFT)
                elif s == '>':
                    moves.append(Dir.RIGHT)
        line = f.readline()
    map = Map(map_lines)
    
map.extend()
# map.print()

for move in moves:
    map.move(move)
    # print(f'Move {move.value}:')
    # map.print()

print(f'Box score: {map.box_score()}')
