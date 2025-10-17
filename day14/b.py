import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'common')))

from util import select_input_file
from a import print_room
from paint import save_paint

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

from collections import defaultdict

def is_dense_by_grid(robot, grid_size=30, ratio_threshold=0.3):
    grid_counts = defaultdict(int)
    for robot in robots:
        grid_x = int(robot.x // grid_size)
        grid_y = int(robot.y // grid_size)
        grid_counts[(grid_x, grid_y)] += 1
    
    max_count = max(grid_counts.values())
    return max_count / len(robots) >= ratio_threshold

        
if __name__ == '__main__':
    # room = Room(11, 7)
    room = Room(101, 103)
    robots = []
    with open(select_input_file(['example.txt', 'input.txt'])) as f:
        for line in f.readlines():
            part = line.strip().split()
            x, y = [int(x) for x in part[0].split('=')[1].split(',')]
            vx, vy = [int(x) for x in part[1].split('=')[1].split(',')]
            robots.append(Robot(x, y, vx, vy, room))

    round = 0
    for _ in range(1000000000):
        for robot in robots:
            robot.move(1)
        round += 1
        print(round)

        if is_dense_by_grid(robots):
            print_room(robots, room)
            if input('continue? (y/n): ') == 'n':
                break
    print(f'round: {round}')
    save_paint([(robot.x, robot.y) for robot in robots], room)
