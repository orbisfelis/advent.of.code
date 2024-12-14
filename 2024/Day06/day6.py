from enum import Enum
from copy import deepcopy

class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

class Day6:

    PUZZLE_MAP = None

    def read_lines(self, filepath: str) -> list:
        return [list(item) for item in [line.rstrip() for line in open(filepath, 'r')]]
    
    def get_start_loc(self):
        for idx_r, row in enumerate(self.PUZZLE_MAP):
            for idx_c, col in enumerate(row):
                if col not in ['.', '#']:
                    return (idx_r, idx_c)
    
    def get_direction(self, location: tuple):
        guard = self.PUZZLE_MAP[location[0]][location[1]]
        if guard == "^":
            return Direction.UP
        elif guard == ">":
            return Direction.RIGHT
        elif guard == "v":
            return Direction.DOWN
        elif guard == "<":
            return Direction.LEFT
    
    def rotate_direction(self, direction: Direction):
        if direction == Direction.UP:
            return Direction.RIGHT
        elif direction == Direction.RIGHT:
            return Direction.DOWN
        elif direction == Direction.DOWN:
            return Direction.LEFT
        elif direction == Direction.LEFT:
            return Direction.UP
    
    def is_exit(self, location: tuple, map: list[list] = None):
        map = map or self.PUZZLE_MAP
        if min(location[0], location[1]) < 0 or max(location[0], location[1]) >= len(map):
            return True
        return False

    def is_obstacle(self, location: tuple, map: list[list] = None):
        map = map or self.PUZZLE_MAP
        if map[location[0]][location[1]] in ['#', 'O']:
            return True
        return False

    def calculate_solution(self, map: list[list]):
        sum = 0
        for idx_r, row in enumerate(map):
            for idx_c, col in enumerate(row):
                if col == 'X':
                    sum += 1
        return sum
    
    def do_slow_move(self, current_dir: Direction, current_loc: tuple, puzzle: list[list] = None):
        puzzle = puzzle or self.PUZZLE_MAP
        next_loc = tuple(map(lambda x, y: x + y, current_loc, current_dir.value))
        if self.is_exit(next_loc, puzzle):
            return current_dir, None
        elif self.is_obstacle(next_loc, puzzle):
            current_dir = self.rotate_direction(current_dir)
            return self.do_slow_move(current_dir, current_loc, puzzle)
        return current_dir, next_loc
    
    def do_fast_move(self, current_dir: Direction, current_loc: tuple, puzzle: list[list] = None):
        puzzle = puzzle or self.PUZZLE_MAP
        first_dir, first_loc = self.do_slow_move(current_dir, current_loc, puzzle)
        if not first_loc:
            return current_dir, None
        else:
            return self.do_slow_move(first_dir, first_loc, puzzle)
    
    def original_guard_path(self):
        solution = deepcopy(self.PUZZLE_MAP)
        current_loc = self.get_start_loc()
        current_dir = self.get_direction(current_loc)

        while current_loc:
            solution[current_loc[0]][current_loc[1]] = 'X'
            current_dir, current_loc = self.do_slow_move(current_dir, current_loc)
        return solution
    
    def part1(self):
        solution = self.original_guard_path()
        print(self.calculate_solution(solution))

    def run_paradox_simulation(self, puzzle: list[list]):
        '''
            Tortoise and Hare - run a slow (normal one) and fast (x2) simulation.
            If slow location == fast location + direction is the same -> fast has caught up to slow and valid obstacle.
            If fast exits field -> go to next possible obstacle placement.
        '''
        slow_loc = self.get_start_loc()
        slow_dir = self.get_direction(slow_loc)

        # Need to do first fast step.
        fast_dir, fast_loc = self.do_fast_move(slow_dir, slow_loc, puzzle)

        while slow_loc and fast_loc and (slow_loc != fast_loc or (slow_loc == fast_loc and slow_dir != fast_dir)):
            slow_dir, slow_loc = self.do_slow_move(slow_dir, slow_loc, puzzle)
            fast_dir, fast_loc = self.do_fast_move(fast_dir, fast_loc, puzzle)
        
        if not fast_loc:
            return False
        
        if slow_loc == fast_loc:
            return fast_loc

    def part2(self):
        '''
            BRUTE FORCE IT! It is extra slow :) - run 2 simulations (slow and fast) for an obstacle in every possible location.
        '''
        solution_locations = []
        obstructed_puzzle = deepcopy(self.PUZZLE_MAP)
        for idx_r, row in enumerate(self.PUZZLE_MAP):
            for idx_c, col in enumerate(row):
                if col == '.':
                    obstructed_puzzle[idx_r][idx_c] = 'O'
                    loc = self.run_paradox_simulation(obstructed_puzzle)
                    if loc:
                        solution_locations.append(loc)
                    obstructed_puzzle[idx_r][idx_c] = '.'
        print(len(solution_locations))
    
    def part2_optimized(self):
        '''
            Only possible placement of obstacles is along the original path of the guard.
            Use those locations to narrow it down.
        '''
        part1_solution = self.original_guard_path()
        part1_solutions_locs = []
        for idx_r, row in enumerate(part1_solution):
            for idx_c, col in enumerate(row):
                if col == 'X':
                    part1_solutions_locs.append((idx_r, idx_c))
        solution_locations = []
        obstructed_puzzle = deepcopy(self.PUZZLE_MAP)
        for locs in part1_solutions_locs:
            idx_r, idx_c = locs
            if obstructed_puzzle[idx_r][idx_c] == '.':
                obstructed_puzzle[idx_r][idx_c] = 'O'
                loc = self.run_paradox_simulation(obstructed_puzzle)
                if loc:
                    solution_locations.append(loc)
                obstructed_puzzle[idx_r][idx_c] = '.'
        print(len(solution_locations))

def main():
    solution = Day6()
    puzzle_map = solution.read_lines("2024/Day6/input.txt")
    solution.PUZZLE_MAP = puzzle_map
    solution.part1()
    # solution.part2()
    solution.part2_optimized()

main()