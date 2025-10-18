from hashlib import new
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
                    self.robot = (x, y)
                
    
    def contains(self, x, y):
        return 0 <= x < len(self.matrix) and 0 <= y < len(self.matrix[x])
    
    def __find_ref(self, refs, x, y, dir: Dir):
        if self.matrix[x][y] == '@':
            refs.add((x, y))

            if dir == Dir.UP:
                self.__find_ref(refs, x-1, y, dir)
            elif dir == Dir.DOWN:
                self.__find_ref(refs, x+1, y, dir)
            elif dir == Dir.LEFT:
                self.__find_ref(refs, x, y-1, dir)
            elif dir == Dir.RIGHT:
                self.__find_ref(refs, x, y+1, dir)
        elif self.matrix[x][y] == '[':
            refs.add((x, y))
            refs.add((x, y+1))

            if dir == Dir.UP:
                self.__find_ref(refs, x-1, y, dir)
                self.__find_ref(refs, x-1, y+1, dir)
            elif dir == Dir.DOWN:
                self.__find_ref(refs, x+1, y, dir)
                self.__find_ref(refs, x+1, y+1, dir)
            elif dir == Dir.LEFT:
                self.__find_ref(refs, x, y-1, dir)
            elif dir == Dir.RIGHT:
                self.__find_ref(refs, x, y+1, dir)
        elif self.matrix[x][y] == ']':
            refs.add((x, y-1))
            refs.add((x, y))

            if dir == Dir.UP:
                self.__find_ref(refs, x-1, y, dir)
                self.__find_ref(refs, x-1, y-1, dir)
            elif dir == Dir.DOWN:
                self.__find_ref(refs, x+1, y, dir)
                self.__find_ref(refs, x+1, y-1, dir)
            elif dir == Dir.LEFT:
                self.__find_ref(refs, x, y-1, dir)
            elif dir == Dir.RIGHT:
                self.__find_ref(refs, x, y+1, dir)
            
    def __can_move(self, refs, dir: Dir) -> bool:
        for pos in refs:
            if dir == Dir.UP:
                if self.matrix[pos[0]-1][pos[1]] == '#':
                    return False
            elif dir == Dir.DOWN:
                if self.matrix[pos[0]+1][pos[1]] == '#':
                    return False
            elif dir == Dir.LEFT:
                if self.matrix[pos[0]][pos[1]-1] == '#':
                    return False
            elif dir == Dir.RIGHT:
                if self.matrix[pos[0]][pos[1]+1] == '#':
                    return False
        return True

    def __move(self, refs: set, dir: Dir):
        while len(refs) > 0:
            pos = refs.pop()
            val = self.matrix[pos[0]][pos[1]]
            if dir == Dir.UP and self.matrix[pos[0]-1][pos[1]] == '.':
                self.matrix[pos[0]][pos[1]] = '.'
                self.matrix[pos[0]-1][pos[1]] = val

                if val == '@':
                    self.robot = (pos[0]-1, pos[1])
            elif dir == Dir.DOWN and self.matrix[pos[0]+1][pos[1]] == '.':
                self.matrix[pos[0]][pos[1]] = '.'
                self.matrix[pos[0]+1][pos[1]] = val

                if val == '@':
                    self.robot = (pos[0]+1, pos[1])
            elif dir == Dir.LEFT and self.matrix[pos[0]][pos[1]-1] == '.':
                self.matrix[pos[0]][pos[1]] = '.'
                self.matrix[pos[0]][pos[1]-1] = val
                
                if val == '@':
                    self.robot = (pos[0], pos[1]-1)
            elif dir == Dir.RIGHT and self.matrix[pos[0]][pos[1]+1] == '.':
                self.matrix[pos[0]][pos[1]] = '.'
                self.matrix[pos[0]][pos[1]+1] = val
                
                if val == '@':
                    self.robot = (pos[0], pos[1]+1)
            else:
                refs.add(pos)
            
    def move(self, dir: Dir):
        refs = set()
        self.__find_ref(refs, self.robot[0], self.robot[1], dir)
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
                moves.append(Dir(s))
        line = f.readline()
    map = Map(map_lines)
    
map.extend()
# map.print()

for move in moves:
    map.move(move)
    # print(f'Move {move.value}:')
    # map.print()

print(f'Box score: {map.box_score()}')
