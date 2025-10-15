
from typing import List


class Map():
    def __init__(self, lines: List[str]):
        self.matrix = []
        for line in lines:
            self.matrix.append(list(line.strip()))
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == "^":
                    self.pos = (i, j)
                    self.dir = (-1, 0)  # up
                    self.walked = [(i, j)]
    
    def move(self) -> bool:
        next_pos = (self.pos[0] + self.dir[0], self.pos[1] + self.dir[1])
        if not (0 <= next_pos[0] < len(self.matrix) and 0 <= next_pos[1] < len(self.matrix[0])):
            return False
        if self.matrix[next_pos[0]][next_pos[1]] == "#":
            if self.dir == (-1, 0):
                self.dir = (0, 1)
            elif self.dir == (0, 1):
                self.dir = (1, 0)
            elif self.dir == (1, 0):
                self.dir = (0, -1)
            elif self.dir == (0, -1):
                self.dir = (-1, 0)
            next_pos = (self.pos[0] + self.dir[0], self.pos[1] + self.dir[1])
            if not (0 <= next_pos[0] < len(self.matrix) and 0 <= next_pos[1] < len(self.matrix[0])):
                return False
            self.pos = next_pos
            self.walked.append(next_pos)
            return True
        elif self.matrix[next_pos[0]][next_pos[1]] in [".", "^"]:
            self.pos = next_pos
            self.walked.append(next_pos)
            return True
        else:
            return False

    @property
    def walked_count(self) -> int:
        return len(set(self.walked))
        
    
        

with open(input("input file name: ")) as f:
    lines = f.readlines()
    map = Map(lines)

while map.move():
    pass

# print(map.walked)
print(map.walked_count)

# print(map.matrix)
# print(map.pos)
