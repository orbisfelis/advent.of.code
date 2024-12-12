from collections import deque, defaultdict
from enum import Enum

class ExtendedEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

class Direction(ExtendedEnum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

class Day12:

    def parse_input(self, filepath: str) -> list:
        return [list(item) for item in [line.rstrip() for line in open(filepath, 'r')]]
    
    def calculate_fences(self, grid, row, col, initial_coord):
        R, C = len(grid), len(grid[0])
        curr_elem = grid[row][col]
        same_neighbors = 0
        borders = defaultdict(list)
        for dir in list(Direction):
            dr, dc = dir.value
            r, c = dr + row, dc + col
            if (r in range(R) and
                c in range(C)):
                if grid[r][c] == curr_elem:
                    same_neighbors += 1
                else:
                    borders[((curr_elem, initial_coord), dir)].append((row, col))
            else:
                borders[((curr_elem, initial_coord), dir)].append((row, col))
        return 4 - same_neighbors, borders

    def count_contiguous_fences(self, fence_blocks: dict):
        '''
            Used in Part2 - calculate contiguous fences for bulk pricing.
        '''
        count = defaultdict(int)
        for flower, fences in fence_blocks.items():
            if flower[1] in [Direction.UP, Direction.DOWN]:
                fences = sorted(fences, key=lambda element: (element[0], element[1]))
                idx = 1
                groups_x = [f[0] for f in fences]
                groups_y = [f[1] for f in fences]
                current_group = 1
                while idx < len(fences):
                    if not (groups_x[idx] == groups_x[idx-1] and groups_y[idx] == groups_y[idx-1] + 1):
                        current_group += 1
                    idx += 1
            elif flower[1] in [Direction.LEFT, Direction.RIGHT]:
                fences = sorted(fences, key=lambda element: (element[1], element[0]))
                idx = 1
                groups_x = [f[0] for f in fences]
                groups_y = [f[1] for f in fences]
                current_group = 1
                while idx < len(fences):
                    if not (groups_y[idx] == groups_y[idx-1] and groups_x[idx] == groups_x[idx-1] + 1):
                        current_group += 1
                    idx += 1
            count[flower[0]] += current_group
        return count

    def solution(self, grid):
        R, C = len(grid), len(grid[0])
        visit = set()
        sizes = defaultdict(int)
        fences = defaultdict(int)
        fences_staging = defaultdict(list)

        def bfs(r, c, initial_node, initial_coord):
            q = deque()
            visit.add((r, c))
            q.append((r, c))
            sizes[(initial_node, initial_coord)] = 1
            fence_counts, fence_borders = self.calculate_fences(grid, r, c, initial_coord)
            fences[(initial_node, initial_coord)] = fence_counts
            for key, value in fence_borders.items():
                fences_staging[key].extend(value)

            while q:
                row, col = q.pop()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(R) and
                        c in range(C) and
                        grid[r][c] == initial_node and
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))
                        sizes[(initial_node, initial_coord)] += 1
                        fence_counts, fence_borders = self.calculate_fences(grid, r, c, initial_coord)
                        fences[(initial_node, initial_coord)] += fence_counts
                        for key, value in fence_borders.items():
                            fences_staging[key].extend(value)
            return

        for r in range(R):
            for c in range(C):
                if (r, c) not in visit:
                    initial_coord = (r, c)
                    initial_node = grid[r][c]
                    bfs(r, c, initial_node, initial_coord)

        fences_bulk = self.count_contiguous_fences(fences_staging)

        total_price = 0
        total_price_bulk = 0
        for key, value in sizes.items():
            area = value
            perimeter = fences[key]
            total_price += area * perimeter
            fence_borders = fences_bulk[key]
            total_price_bulk += area * fence_borders

        print(f"Total Price - Part 1: {total_price}")
        print(f"Total Bulk Fence Price - Part 2: {total_price_bulk}")
        
def main():
    solution = Day12()
    grid = solution.parse_input("2024/Day12/input.txt")
    solution.solution(grid)

main()