import itertools
from enum import Enum
from collections import deque

class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

class Day20:

    def parse_input(self, filepath: str) -> list:
        return [list(item) for item in [line.rstrip() for line in open(filepath, 'r')]]
    
    def get_start(self, grid):
        for idx_r, row in enumerate(grid):
            for idx_c, col in enumerate(row):
                if col == "S":
                    return (idx_r, idx_c)
    
    def get_end(self, grid):
        for idx_r, row in enumerate(grid):
            for idx_c, col in enumerate(row):
                if col == "E":
                    return (idx_r, idx_c)
    
    def generate_scores(self, grid):
        r, c = self.get_start(grid)
        R, C = len(grid), len(grid[0])
        q = deque()
        scores = dict()
        visit = set()

        scores[(r, c)] = 0
        visit.add((r, c))
        q.append((r, c, 0))

        while q:
            row, col, curr_steps = q.popleft()
            if grid[row][col] == "E":
                return scores
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                new_score = curr_steps+1
                r, c = row + dr, col + dc
                if (r in range(R) and c in range(C) and
                    (r, c) not in visit and grid[r][c] != '#'):
                    q.append((r, c, new_score))
                    visit.add((r, c))
                    scores[(r, c)] = new_score
        return

    def find_cheats(self, scores, pico=2):
        '''
            Pre-calculated scores for each step in the maze.
            For each position, get furthest position reachable within X seconds.
            Use the manhattan distance to calculate distance between points.
        '''
        cheats = dict()
        all_combinations = itertools.combinations(list(scores), 2)
        for combo in all_combinations:
            point1 = combo[0]
            point2 = combo[1]
            manhattan_dist = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
            if manhattan_dist <= pico:
                cheats[combo] = scores[point2] - scores[point1] - manhattan_dist
        return cheats


    def solution(self, scores, threshold, pico):
        cheats = self.find_cheats(scores, pico)
        cheat_counts = 0
        for cheat_count in cheats.values():
            if cheat_count >= threshold:
                cheat_counts += 1
        print(cheat_counts)
        

def main():
    solution = Day20()
    threshold = 100
    grid = solution.parse_input("2024/Day20/input.txt")
    scores = solution.generate_scores(grid)
    solution.solution(scores, threshold, 2) # Part 1
    solution.solution(scores, threshold, 20) # Part 2

main()