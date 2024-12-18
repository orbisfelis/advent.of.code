from collections import deque
from enum import Enum
from copy import deepcopy

class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

class Day18:

    def parse_input(self, filepath: str) -> list:
        return [tuple(map(int, line.rstrip().split(","))) for line in open(filepath, 'r')]
    
    def bfs(self, grid, start_coords, end_coords):
        R, C = len(grid), len(grid[0])
        r, c = start_coords
        results = list()
        q = deque()
        scores = dict()
        visit = set()

        scores[(r, c)] = 0
        visit.add((r, c))
        q.append((r, c, 0))

        while q:
            row, col, curr_steps = q.popleft()
            if (row, col) == end_coords:
                results.append(curr_steps)
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                new_score = curr_steps+1
                r, c = row + dr, col + dc
                if (r in range(R) and
                    c in range(C) and
                    ((r, c) not in visit or scores.get((r, c), float("infinity")) > new_score) and
                    grid[r][c] != '#'):
                    q.append((r, c, new_score))
                    visit.add((r, c))
                    scores[(r, c)] = new_score
        return results

    def solution(self, R, C, obstacles, part1=True):
        grid = [["." for _ in range(R)] for _ in range(C)]
        for obstacle in obstacles[:1024]:
            x, y = obstacle
            grid[x][y] = "#"
        if part1:
            print(min(self.bfs(grid, (0, 0), (70, 70))))
        else:
            l, r = 1024, len(obstacles) - 1
            while l <= r:
                new_grid = deepcopy(grid)
                mid = (l + r) // 2
                print(f'Trying {mid}')
                for idx in range(1024, mid):
                    x, y = obstacles[idx]
                    new_grid[x][y] = '#'
                results = self.bfs(new_grid, (0, 0), (70, 70))
                if not results:
                    r = mid - 1
                else:
                    l = mid + 1
            print(obstacles[mid-1])
        
def main():
    solution = Day18()
    # obstacles = solution.parse_input("2024/Day18/test_input.txt")
    # solution.solution(7, 7, obstacles[:12])
    obstacles = solution.parse_input("2024/Day18/input.txt")
    solution.solution(71, 71, obstacles, part1=True)
    solution.solution(71, 71, obstacles, part1=False)

main()