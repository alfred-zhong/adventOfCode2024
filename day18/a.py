from enum import Enum
import heapq
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'common')))

from util import select_input_file


class Map():
    def __init__(self, x, y):
        self.grid = []
        for i in range(x):
            self.grid.append(['.'] * y)
        self.start = (0, 0)
        self.end = (x - 1, y - 1)

    def __is_valid(self, x, y):
        return 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0])
        
    def add_broken(self, pos):
        self.grid[pos[0]][pos[1]] = '#'

    def walk(self):
        # state (score, x, y)
        queue = [(0, *self.start)]
        seen = set()
        while queue:
            score, x, y = heapq.heappop(queue)
            print(f'scan: ({x}, {y})')

            if (x, y) in seen:
                continue
            else:
                seen.add((x, y))

            if (x, y) == self.end:
                return score
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if self.__is_valid(x + dx, y + dy) and self.grid[x + dx][y + dy] != '#' and (x + dx, y + dy) not in seen:
                    heapq.heappush(queue, (score + 1, x + dx, y + dy))


pre = {
    "example1.txt": {
        "size": 7,
        "broken": 12,
    },
    "input.txt": {
        "size": 71,
        "broken": 1024,
    },
}

key = select_input_file(pre.keys())
with open(key) as f:
    brokens = []
    for line in f.readlines():
        brokens.append(tuple(map(int, line.strip().split(','))))

map = Map(pre[key]['size'], pre[key]['size'])
for i in range(pre[key]['broken']):
    map.add_broken(brokens[i])

print(map.walk())
