import itertools

class Day4:

    def read_lines(self, filepath: str) -> list:
        return [line.rstrip() for line in open(filepath, 'r')]
    
    def part1(self, puzzle: list, words: list):
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
        pass

def main():
    solution = Day4()
    puzzle = solution.read_lines("2024/Day 4/input.txt")
    solution.part1(puzzle, ['XMAS'])
    solution.part2(puzzle)

main()