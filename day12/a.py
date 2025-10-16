import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'common')))

from util import select_input_file

def connect(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) == 1

def connect_region(pos, region):
    for r in region:
        if connect(pos, r):
            return True
    return False

def regions_connected(region1, region2):
    for r1 in region1:
        if connect_region(r1, region2):
            return True
    return False

class Garden():
    def __init__(self, lines):
        self.matrix = []
        for line in lines:
            self.matrix.append([x for x in line.strip()])
            self.arranged = set()
            self.regions = []
    
    def is_valid_pos(self, pos):
        return pos[0] >= 0 and pos[0] < len(self.matrix) and pos[1] >= 0 and pos[1] < len(self.matrix[0])
    
    def scan(self, region, pos):
        if pos in self.arranged:
            return

        if len(region) == 0:
            region = [pos]
            self.regions.append(region)
        else:
            region.append(pos)
        self.arranged.add(pos)
        
        left = (pos[0], pos[1] - 1)
        if self.is_valid_pos(left) and self.matrix[left[0]][left[1]] == self.matrix[pos[0]][pos[1]]:
            self.scan(region, left)

        right = (pos[0], pos[1] + 1)
        if self.is_valid_pos(right) and self.matrix[right[0]][right[1]] == self.matrix[pos[0]][pos[1]]:
            self.scan(region, right)

        up = (pos[0] - 1, pos[1])
        if self.is_valid_pos(up) and self.matrix[up[0]][up[1]] == self.matrix[pos[0]][pos[1]]:
            self.scan(region, up)

        down = (pos[0] + 1, pos[1])
        if self.is_valid_pos(down) and self.matrix[down[0]][down[1]] == self.matrix[pos[0]][pos[1]]:
            self.scan(region, down)
        

    
    def calc_regions(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.scan([], (i, j))
        
        
def calc_region_perimeter(region):
    perimeter = 4 * len(region)
    for i in range(len(region)):
        for j in range(len(region)):
            if i != j and connect(region[i], region[j]):
                perimeter -= 1
    return perimeter
    
    


with open(select_input_file(['example1.txt', 'example2.txt', 'example3.txt', 'input.txt'])) as f:
    garden = Garden(f.readlines())

garden.calc_regions()

costs = 0
for region in garden.regions:
    print(region)
    perimeter = calc_region_perimeter(region)
    costs += perimeter*len(region)

print(f'costs: {costs}')

