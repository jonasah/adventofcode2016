from enum import IntEnum
import copy

INPUT = "R3, L5, R1, R2, L5, R2, R3, L2, L5, R5, L4, L3, R5, L1, R3, R4, R1, L3, R3, L2, L5, L2, R4, R5, R5, L4, L3, L3, R4, R4, R5, L5, L3, R2, R2, L3, L4, L5, R1, R3, L3, R2, L3, R5, L194, L2, L5, R2, R1, R1, L1, L5, L4, R4, R2, R2, L4, L1, R2, R53, R3, L5, R72, R2, L5, R3, L4, R187, L4, L5, L2, R1, R3, R5, L4, L4, R2, R5, L5, L4, L3, R5, L2, R1, R1, R4, L1, R2, L3, R5, L4, R2, L3, R1, L4, R4, L1, L2, R3, L1, L1, R4, R3, L4, R2, R5, L2, L3, L3, L1, R3, R5, R2, R3, R1, R2, L1, L4, L5, L2, R4, R5, L2, R4, R4, L3, R2, R1, L4, R3, L3, L4, L3, L1, R3, L2, R2, L4, L4, L5, R3, R5, R3, L2, R5, L2, L1, L5, L1, R2, R4, L5, R2, L4, L5, L4, L5, L2, L5, L4, R5, R3, R2, R2, L3, R3, L2, L5"

class Direction(IntEnum):
    EAST = 1
    WEST = 2
    NORTH = 3
    SOUTH = 4

class GridPosition:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = Direction.NORTH

    def turn_left(self):
        if self.direction == Direction.NORTH:
            self.direction = Direction.WEST
        elif self.direction == Direction.WEST:
            self.direction = Direction.SOUTH
        elif self.direction == Direction.SOUTH:
            self.direction = Direction.EAST
        else:
            self.direction = Direction.NORTH

    def turn_right(self):
        if self.direction == Direction.NORTH:
            self.direction = Direction.EAST
        elif self.direction == Direction.EAST:
            self.direction = Direction.SOUTH
        elif self.direction == Direction.SOUTH:
            self.direction = Direction.WEST
        else: # WEST
            self.direction = Direction.NORTH

    def walk(self, num_blocks):
        if self.direction == Direction.NORTH:
            self.y += num_blocks
        elif self.direction == Direction.EAST:
            self.x += num_blocks
        elif self.direction == Direction.SOUTH:
            self.y -= num_blocks
        else: # WEST
            self.x -= num_blocks

    def distance(self):
        return abs(self.x) + abs(self.y)


def main():
    pos = GridPosition()
    history = []
    part2 = None

    for command in INPUT.split(', '):
        direction = command[0]
        blocks = int(command[1:])

        if direction == 'R':
            pos.turn_right()
        else:
            pos.turn_left()

        for _ in range(0, blocks):
            pos.walk(1)
            coord = (pos.x, pos.y)
            if coord in history and part2 is None:
                part2 = copy.deepcopy(pos)
            else:
                history.append(coord)

    print("Part 1:", pos.x, pos.y, "=>", pos.distance())
    print("Part 2:", part2.x, part2.y, "=>", part2.distance())

if __name__ == '__main__':
    main()
