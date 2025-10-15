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
    
    def in_map(self, a):
        return 0 <= a[0] < len(self.matrix) and 0 <= a[1] < len(self.matrix[0])
    
    def pair_antinodes(self, a, b):
        nodes = [a, b]

        delta = (a[0] - b[0], a[1] - b[1])
        new_node = (a[0] + delta[0], a[1] + delta[1])
        while self.in_map(new_node):
            nodes.append(new_node)
            new_node = (new_node[0] + delta[0], new_node[1] + delta[1])

        delta = (b[0] - a[0], b[1] - a[1])
        new_node = (b[0] + delta[0], b[1] + delta[1])
        while self.in_map(new_node):
            nodes.append(new_node)
            new_node = (new_node[0] + delta[0], new_node[1] + delta[1])
        
        return nodes
        
                                

with open(select_input_file(['example.txt', 'example1.txt', 'input.txt'])) as f:
    m = Map(f.readlines())

# print(m.matrix)
# print(m.antennas)
print(m.antinodes)
print(len(m.antinodes))
