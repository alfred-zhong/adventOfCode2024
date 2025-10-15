
from enum import Enum
from typing import List, Tuple

class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

def change_direction(current: Direction) -> Direction:
    if current == Direction.UP:
        return Direction.RIGHT
    elif current == Direction.RIGHT:
        return Direction.DOWN
    elif current == Direction.DOWN:
        return Direction.LEFT
    elif current == Direction.LEFT:
        return Direction.UP

class Position():
    def __init__(self, i: int, j: int):
        self.i = i
        self.j = j
    
    def __add__(self, other: Tuple[int, int]):
        return Position(self.i + other[0], self.j + other[1])

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j
    
    def __hash__(self):
        return hash((self.i, self.j))

class Vector():
    def __init__(self, start: Position, direction: Direction):
        self.start = start
        self.direction = direction

    def move(self) -> Position:
        self.start += self.direction.value
        return self.start

    def change_direction(self, new_direction: Direction):
        self.direction = new_direction

    def __eq__(self, other):
        return self.start == other.start and self.direction == other.direction
    
    def __hash__(self):
        return hash((self.start, self.direction))

class Map():
    def __init__(self, lines: List[str]):
        self.matrix = []
        for line in lines:
            self.matrix.append(list(line.strip()))
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == "^":
                    self.pos = Position(i, j)
                    self.dir = Direction.UP
                    self.walked = set([self.pos])
                    self.loops = set([Vector(self.pos, self.dir)])
    
    def move(self) -> Tuple[bool, bool]:
        next_pos = self.pos + self.dir.value
        if not (0 <= next_pos.i < len(self.matrix) and 0 <= next_pos.j < len(self.matrix[0])):
            return False, False
        if self.matrix[next_pos.i][next_pos.j] == "#":
            self.dir = change_direction(self.dir)
            next_pos = self.pos + self.dir.value
            if not (0 <= next_pos.i < len(self.matrix) and 0 <= next_pos.j < len(self.matrix[0])):
                return False, False
            
            if self.matrix[next_pos.i][next_pos.j] == "#":
                self.dir = change_direction(self.dir)
                next_pos = self.pos + self.dir.value
                if not (0 <= next_pos.i < len(self.matrix) and 0 <= next_pos.j < len(self.matrix[0])):
                    return False, False

            self.pos = next_pos
            self.walked.add(next_pos)
            
            if Vector(self.pos, self.dir) in self.loops:
                return True, True

            self.loops.add(Vector(self.pos, self.dir))
            return True, False
        elif self.matrix[next_pos.i][next_pos.j] in [".", "^"]:
            self.pos = next_pos
            self.walked.add(next_pos)
            if Vector(self.pos, self.dir) in self.loops:
                return True, True

            self.loops.add(Vector(self.pos, self.dir))
            return True, False
        else:
            return False, False
    
    def is_loop(self) -> bool:
        still_in, loop = map.move()
        while still_in:
            if loop:
                return True
            still_in, loop = map.move()
        return False
    
        
with open(input("input file name: ")) as f:
    lines = f.readlines()
    map = Map(lines)

print(map.is_loop())
walked = map.walked
print(f'walked count: {len(walked)}')

loop_count = 0
count = 0
for w in walked:
    i, j = w.i, w.j
    if lines[i][j] in ["."]:
        new_lines = lines.copy()
        new_lines[i] = new_lines[i][:j] + "#" + new_lines[i][j+1:]
        map = Map(new_lines)
        count += 1
        print(f'count: {count}')
        if map.is_loop():
            loop_count += 1
            # print(loop_count)

print(loop_count)
