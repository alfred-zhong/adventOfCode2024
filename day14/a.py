import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'common')))

from util import select_input_file

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
            
    for robot in robots:
        robot.move(100)
        print(robot)

    quadrant_counts = [0, 0, 0, 0, 0]
    for robot in robots:
        quadrant_counts[robot.quadrant] += 1
    print(quadrant_counts)

    import math
    factor = math.prod(quadrant_counts[1:])
    print(f'factor: {factor}')

    '''
    r = Robot(2, 4, 2, -3, Room(11, 7))
    for _ in range(5):
        r.move(1)
        print(r)
    '''

def print_room(robots, room):
    counters = set()
    for robot in robots:
        counters.add((robot.x, robot.y))
    for y in range(room.y):
        for x in range(room.x):
            if (x, y) in counters:
                print('#', end='')
            else:
                print('.', end='')
        print()

# print_room(robots, room)
