import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'common')))

from util import select_input_file
import heapq

class Map():
    def __init__(self, lines):
        self.grid = []
        for line in lines:
            self.grid.append(line.strip())

        found = False
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 'S':
                    self.start = (i, j)
                    found = True
                    break
            if found:
                break
    
    def get_best_score(self):
        # (costs, x, y, dx, dy)
        queue = [(0, *self.start, 0, 1)]
        seen = set()
        while queue:
            costs, x, y, dx, dy = heapq.heappop(queue)
            seen.add((x, y, dx, dy))
            print(f'visiting: ({x}, {y})')
            if self.grid[x][y] == 'E':
                return costs
            
            if self.grid[x + dx][y + dy] != '#' and (x + dx, y + dy, dx, dy) not in seen:
                heapq.heappush(queue, (costs + 1, x + dx, y + dy, dx, dy))
            for new_dx, new_dy in [(-dy, dx), (dy, -dx)]:
                if self.grid[x + new_dx][y + new_dy] != '#' and (x, y, new_dx, new_dy) not in seen:
                    heapq.heappush(queue, (costs + 1000, x, y, new_dx, new_dy))
    
    

with open(select_input_file(['example1.txt', 'example2.txt','input.txt'])) as f:
    map = Map(f.readlines())

print(f'costs: {map.get_best_score()}')
