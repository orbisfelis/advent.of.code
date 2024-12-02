
class Day2:

    def read_lines(self, filepath: str):
        return [line.rstrip() for line in open("2024/Day 2/input.txt", 'r')]

    def is_safe(self, report: list):
        sort = sorted(report)
        if report != sort[::-1] and report != sort:
            return False
        return all(1 <= d <= 3 for d in [abs(x-y) for x,y in list(zip(report[1:], report[:-1]))])

    def part1(self, lines):
        safeCounter = 0
        for line in lines:
            report = list(map(int, line.split()))
            safeCounter += 1 if self.is_safe(report) else 0
        print(safeCounter)
    
    def part2(self):
        pass

def main():
    solution = Day2()
    lines = solution.read_lines("2024/Day 2/input.txt")
    solution.part1(lines)
    solution.part2()

main()