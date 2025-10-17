import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'common')))

from util import select_input_file
from a import print_room

class Room():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Robot():
    def __init__(self, x, y, vx, xy, room):
        self.x = x
        self.y = y
        self.vx = vx
        self.xy = xy
        self.room = room
    
    def move(self, round: int):
        self.x = (self.x + self.vx * round) % self.room.x
        self.y = (self.y + self.xy * round) % self.room.y
    
    def __str__(self):
        return f'Robot({self.x}, {self.y})'
    
    def __repr__(self):
        return self.__str__()
    
    @property
    def quadrant(self):
        '''
        1 2
        3 4
        '''
        
        if self.x < self.room.x // 2:
            if self.y < self.room.y // 2:
                return 1
            elif self.y > self.room.y // 2:
                return 3
            else:
                return 0
        elif self.x > self.room.x // 2:
            if self.y < self.room.y // 2:
                return 2
            elif self.y > self.room.y // 2:
                return 4
            else:
                return 0
        else:
            return 0

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def save_paint(points, room):
    # x, y = zip(*points)
    fig, ax = plt.subplots()
    for x, y in points:
        rect = Rectangle((x - 0.5, y - 0.5), 1, 1, color='blue')
        ax.add_patch(rect)

    ax.set_title("Christmas Tree")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_xlim(0, room.x)
    ax.set_ylim(0, room.y)
    ax.invert_yaxis()  # y 轴从上到下
    ax.grid(True)
    plt.savefig("christmas_tree.png", dpi=300, bbox_inches='tight')


if __name__ == '__main__':
    room = Room(11, 7)
    # room = Room(101, 103)
    robots = []
    with open(select_input_file(['example.txt', 'input.txt'])) as f:
        for line in f.readlines():
            part = line.strip().split()
            x, y = [int(x) for x in part[0].split('=')[1].split(',')]
            vx, vy = [int(x) for x in part[1].split('=')[1].split(',')]
            robots.append(Robot(x, y, vx, vy, room))
    
    paint_room([(robot.x, robot.y) for robot in robots], room)
