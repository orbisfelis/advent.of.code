import itertools

class Day4:

    def read_lines(self, filepath: str) -> list:
        return [line.rstrip() for line in open(filepath, 'r')]
    
    def part1(self, puzzle: list):
        R, C = len(puzzle), len(puzzle[0])

        def checkWord(row, col, row_end, col_end, diag=False):
            if (min(row_end, col_end) < 0 or
                row_end >= R or col_end >= C):
                return 0

            word = ""
            row_iterator_dir = -1 if row_end < row else 1
            col_iterator_dir = -1 if col_end < col else 1
            if diag:
                for r, c in zip(range(row, row_end + row_iterator_dir, row_iterator_dir), range(col, col_end + col_iterator_dir, col_iterator_dir)):
                    word += puzzle[r][c]
            else:
                for r, c in itertools.product(range(row, row_end + row_iterator_dir, row_iterator_dir), range(col, col_end + col_iterator_dir, col_iterator_dir)):
                    word += puzzle[r][c]
            
            return int(word == 'XMAS')
            
        res = 0
        for r in range(R):
            for c in range(C):
                if puzzle[r][c] == 'X':
                    for row_dir, col_dir in [(0, 3), (0, -3), (3, 0), (-3, 0)]:
                        row_end, col_end = r + row_dir, c + col_dir
                        res += checkWord(r, c, row_end, col_end)
                    for row_dir, col_dir in [(3, 3), (-3, -3), (3, -3), (-3, 3)]:
                        row_end, col_end = r + row_dir, c + col_dir
                        res += checkWord(r, c, row_end, col_end, diag=True)
        print(res)

    def part2(self, puzzle: list):
        R, C = len(puzzle), len(puzzle[0])

        def checkWord(row, col):
            if (min(row-1, col-1) < 0 or
                row+1 >= R or col+1 >= C):
                return 0

            rightBottom = puzzle[row+1][col+1]
            leftTop = puzzle[row-1][col-1]
            leftBottom = puzzle[row+1][col-1]
            rightTop = puzzle[row-1][col+1]

            for side in [rightTop, leftBottom, leftTop, rightBottom]:
                if side not in ['M', 'S']:
                    return 0
            
            if (((rightTop == 'M' and leftBottom == 'S') or (rightTop == 'S' and leftBottom == 'M')) and
                ((leftTop == 'M' and rightBottom == 'S') or (leftTop == 'S' and rightBottom == 'M'))):
                return 1
            else:
                return 0

        res = 0
        for r in range(R):
            for c in range(C):
                if puzzle[r][c] == 'A':
                    res += checkWord(r, c)
        print(res)

def main():
    solution = Day4()
    puzzle = solution.read_lines("2024/Day 4/input.txt")
    solution.part1(puzzle)
    solution.part2(puzzle)

main()