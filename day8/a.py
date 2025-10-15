import sys, os
import itertools
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'common')))

from util import select_input_file


class Map():
    def __init__(self, lines):
        self.matrix = []
        for line in lines:
            self.matrix.append([x for x in line.strip()])
        self.calc_antennas()
        self.calc_antinodes()
    
    def calc_antennas(self):
        self.antennas = {}
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] not in ['.']:
                    key = self.matrix[i][j]
                    if key in self.antennas:
                        self.antennas[key].add((i, j))
                    else:
                        self.antennas[key] = set([(i, j)])
    
    def calc_antinodes(self):
        self.antinodes = set()
        for key, positions in self.antennas.items():
            for pair in itertools.combinations(positions, 2):
                self.antinodes.update(self.pair_antinodes(pair[0], pair[1]))
    
    def pair_antinodes(self, a, b):
        nodes = []
        n1 = (a[0] + (a[0] - b[0]), a[1] + (a[1] - b[1]))
        if 0 <= n1[0] < len(self.matrix) and 0 <= n1[1] < len(self.matrix[0]):
            nodes.append(n1)
        n2 = (b[0] + (b[0] - a[0]), b[1] + (b[1] - a[1]))
        if 0 <= n2[0] < len(self.matrix) and 0 <= n2[1] < len(self.matrix[0]):
            nodes.append(n2)
        return nodes
        
                                

with open(select_input_file()) as f:
    m = Map(f.readlines())

# print(m.matrix)
# print(m.antennas)
# print(m.antinodes)
print(len(m.antinodes))
