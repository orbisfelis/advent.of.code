from enum import Enum
from collections import deque, defaultdict

class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

class Day16:

    CURRENT_GRID = None

    def parse_input(self, filepath: str) -> list:
        return [list(item) for item in [line.rstrip() for line in open(filepath, 'r')]]
    
    def get_start(self):
        for idx_r, row in enumerate(self.CURRENT_GRID):
            for idx_c, col in enumerate(row):
                if col == "S":
                    return (idx_r, idx_c)
    
    def get_opposites(self):
        return {Direction.UP: Direction.DOWN,
                Direction.DOWN: Direction.UP,
                Direction.LEFT: Direction.RIGHT,
                Direction.RIGHT: Direction.LEFT}

    def get_neighbors(self):
        return {Direction.UP: [Direction.LEFT, Direction.RIGHT],
                Direction.DOWN: [Direction.LEFT, Direction.RIGHT],
                Direction.LEFT: [Direction.UP, Direction.DOWN],
                Direction.RIGHT: [Direction.UP, Direction.DOWN]}

    def solution(self):
        start_r_idx, start_c_idx = self.get_start()
        results = list()

        def bfs(start_r, start_c, curr_direction):
            q = deque()
            visit = set()
            scores = dict()
            visit.add((start_r, start_c))
            q.append((start_r, start_c, [], curr_direction, 0))

            while q:
                row, col, prev_items, curr_direction, curr_score = q.popleft()
                # print((row, col, prev_items, curr_direction))

                if self.CURRENT_GRID[row][col] == "E":
                    results.append((curr_score, prev_items))
                    continue

                directions = [Direction.DOWN, Direction.UP, Direction.LEFT, Direction.RIGHT]
                for dir in directions:
                    dr, dc = dir.value
                    r, c = row + dr, col + dc
                    if self.CURRENT_GRID[r][c] != '#' and self.get_opposites()[curr_direction] != dir:
                        new_score = curr_score + 1
                        if dir in self.get_neighbors()[curr_direction]:
                            new_score += 1000
                            if prev_items:
                                prev_item = prev_items[-1]
                                scores[(prev_item[0], prev_item[1])] += 1000
                        scores[(row, col)] = new_score
                        if ((r, c) not in visit or scores.get((r, c), float("infinity")) > new_score):
                            visit.add((r, c))
                            path = prev_items.copy()
                            path.append((row, col))
                            q.append((r, c, path, dir, new_score))
            return

        bfs(start_r_idx, start_c_idx, Direction.RIGHT)
        min_res = min([val[0] for val in results])
        print(f"Part 1: {min_res}")
        new_res = [res for res in results if res[0] == min_res]
        final_res = []
        for test in new_res:
            final_res = final_res + test[1]
        print(f"Part 2: {len(list(set(final_res))) + 1}")

def main():
    solution = Day16()
    grid = solution.parse_input("2024/Day16/input.txt")
    solution.CURRENT_GRID = grid
    solution.solution()

main()