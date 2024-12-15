import itertools
from enum import Enum

class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

class Day15:

    CURRENT_GRID = None

    def get_direction(self, direction: str):
        if direction == "^":
            return Direction.UP
        elif direction == ">":
            return Direction.RIGHT
        elif direction == "v":
            return Direction.DOWN
        elif direction == "<":
            return Direction.LEFT

    def parse_input(self, filepath: str) -> list:
        grid = []
        movements = []
        for line in open(filepath, 'r'):
            stripped_line = list(line.rstrip())
            if not stripped_line:
                continue
            elif '#' in stripped_line:
                grid.append(stripped_line)
            else:
                movements.append(stripped_line)
        return grid, [self.get_direction(direction) for direction in itertools.chain.from_iterable(movements)]
    
    def get_robot_loc(self):
        for idx_r, row in enumerate(self.CURRENT_GRID):
            for idx_c, col in enumerate(row):
                if col == "@":
                    return (idx_r, idx_c)

    def move_in_direction(self, current_loc_idx, current_val, prev_val, move):
        next_loc_idx = (current_loc_idx[0] + move.value[0], current_loc_idx[1] + move.value[1])
        next_loc = self.CURRENT_GRID[next_loc_idx[0]][next_loc_idx[1]]
        if next_loc == "#":
            return current_loc_idx, False

        if current_val in ["@", "O"]:
            if next_loc == '.':
                self.CURRENT_GRID[next_loc_idx[0]][next_loc_idx[1]] = current_val
                self.CURRENT_GRID[current_loc_idx[0]][current_loc_idx[1]] = prev_val
                return next_loc_idx, True
            elif next_loc == 'O':
                next_loc_idx, movement = self.move_in_direction(next_loc_idx, "O", current_val, move)
                if not movement:
                    return current_loc_idx, False
                else:
                    if current_val != "@":
                        self.CURRENT_GRID[next_loc_idx[0]][next_loc_idx[1]] = current_val
                    self.CURRENT_GRID[current_loc_idx[0]][current_loc_idx[1]] = prev_val
                    return next_loc_idx, True
        
        return current_loc_idx, False

    def calculate_gps(self):
        sum = 0
        for idx_r, row in enumerate(self.CURRENT_GRID):
            for idx_c, col in enumerate(row):
                if col == "O":
                    sum += (idx_r * 100 + idx_c)
        return sum
    
    def part1(self, movements):
        for move in movements:
            current_loc_idx = self.get_robot_loc()
            current_loc_idx, _ = self.move_in_direction(current_loc_idx, "@", ".", move)
        print(self.CURRENT_GRID)
        print(self.calculate_gps())

def main():
    solution = Day15()
    grid, movements = solution.parse_input("2024/Day15/input.txt")
    solution.CURRENT_GRID = grid
    solution.part1(movements)

main()