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
    
def calc_edges(region):
    single_corners, shared_corners = 0, 0
    
    for pos in region:
        '''
        1 2 3
        4 x 5
        6 7 8
        '''
        pos_1 = (pos[0] - 1, pos[1] - 1)
        pos_2 = (pos[0] - 1, pos[1])
        pos_3 = (pos[0] - 1, pos[1] + 1)
        pos_4 = (pos[0], pos[1] - 1)
        pos_5 = (pos[0], pos[1] + 1)
        pos_6 = (pos[0] + 1, pos[1] - 1)
        pos_7 = (pos[0] + 1, pos[1])
        pos_8 = (pos[0] + 1, pos[1] + 1)

        # top_left
        top_left_count = len(list(filter(lambda x: x in (pos_1, pos_2, pos_4), region)))
        if top_left_count == 0:
            single_corners += 1
        elif top_left_count == 1 and pos_1 in region:
            single_corners += 1
        elif top_left_count == 2:
            shared_corners += 1
        # top_right
        top_right_count = len(list(filter(lambda x: x in (pos_2, pos_3, pos_5), region)))
        if top_right_count == 0:
            single_corners += 1
        elif top_right_count == 1 and pos_3 in region:
            single_corners += 1
        elif top_right_count == 2:
            shared_corners += 1
        # bottom_left
        bottom_left_count = len(list(filter(lambda x: x in (pos_4, pos_6, pos_7), region)))
        if bottom_left_count == 0:
            single_corners += 1
        elif bottom_left_count == 1 and pos_6 in region:
            single_corners += 1
        elif bottom_left_count == 2:
            shared_corners += 1
        # bottom_right
        bottom_right_count = len(list(filter(lambda x: x in (pos_5, pos_7, pos_8), region)))
        if bottom_right_count == 0:
            single_corners += 1
        elif bottom_right_count == 1 and pos_8 in region:
            single_corners += 1
        elif bottom_right_count == 2:
            shared_corners += 1
    
    return single_corners + (shared_corners // 3)

        
with open(select_input_file(['example1.txt', 'example2.txt', 'example3.txt', 'input.txt'])) as f:
    garden = Garden(f.readlines())

garden.calc_regions()

costs = 0
for region in garden.regions:
    print(region)
    edges = calc_edges(region)
    costs += edges*len(region)

print(f'costs: {costs}')

# print(calc_edges([(0, 0), (0, 1), (1, 1)]))

