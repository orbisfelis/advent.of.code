
class Day2:

    def read_lines(self, filepath: str) -> list:
        return [line.rstrip() for line in open("2024/Day 2/input.txt", 'r')]

    def is_safe(self, report: list) -> bool:
        # Sort report, check if original is the same in both directions.
        sort = sorted(report)
        if report != sort[::-1] and report != sort:
            return False
        return all(1 <= d <= 3 for d in [abs(x-y) for x,y in list(zip(report[1:], report[:-1]))])

    def is_safe_with_dampener(self, report: list) -> bool:
        if self.is_safe(report):
            return True
        # Very inefficient - check with every possible item removed. n^2
        for idx, _ in enumerate(report):
            subreport = report.copy()
            subreport.pop(idx)
            if self.is_safe(subreport):
                return True
        return False

    def part1(self, report_lines: list) -> int:
        safeCounter = 0
        for line in report_lines:
            report = list(map(int, line.split()))
            safeCounter += 1 if self.is_safe(report) else 0
        return safeCounter
    
    def part2(self, report_lines: list):
        safeCounter = 0
        for line in report_lines:
            report = list(map(int, line.split()))
            safeCounter += 1 if self.is_safe_with_dampener(report) else 0
        return safeCounter

def main():
    solution = Day2()
    report_lines = solution.read_lines("2024/Day 2/input.txt")
    safe_count = solution.part1(report_lines)
    print(safe_count)
    safe_count_with_dampener = solution.part2(report_lines)
    print(safe_count_with_dampener)

main()