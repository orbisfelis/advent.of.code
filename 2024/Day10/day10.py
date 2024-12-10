from collections import defaultdict

class Day10:

    def parse_input(self, filepath: str) -> list:
        return [list(map(int, list(item))) for item in [line.rstrip() for line in open(filepath, 'r')]]
    
    def part1(self, grid):
        R, C = len(grid), len(grid[0])

        result_sets = defaultdict(set)

        def dfs(r, c, prev, visit, start_node):
            if (min(r, c) < 0 or
                r == R or c == C or
                (r, c) in visit or (prev is not None and grid[r][c] - 1 != prev)):
                return 0

            if grid[r][c] == 9:
                result_sets[start_node].add((r, c))
                return 1

            visit.add((r, c))

            count = 0
            count += dfs(r + 1, c, grid[r][c], visit, start_node)
            count += dfs(r - 1, c, grid[r][c], visit, start_node)
            count += dfs(r, c + 1, grid[r][c], visit, start_node)
            count += dfs(r, c - 1, grid[r][c], visit, start_node)

            visit.remove((r, c))
            return count

        visited = set()
        distinct_paths = 0
        for row in range(R):
            for col in range(C):
                if grid[row][col] == 0:
                    distinct_paths += dfs(row, col, None, visited, (row, col))
        
        # Accidently solved part2 here as well.
        print(distinct_paths)
        
        res = 0
        for distinct_ends in result_sets.values():
            res += len(list(distinct_ends))
        print(res)

def main():
    solution = Day10()
    grid = solution.parse_input("2024/Day10/input.txt")
    solution.part1(grid)

main()