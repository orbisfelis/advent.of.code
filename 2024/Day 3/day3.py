import re

class Day3:

    def read_lines(self, filepath: str) -> list:
        return [line.rstrip() for line in open("2024/Day 3/input.txt", 'r')]
    
    def part1(self, report_lines: list):
        pattern = re.compile("mul\(\d+,\d+\)")
        pattern_match = r"mul\((\d+),(\d+)\)"
        sum = 0
        for line in report_lines:
            results = pattern.findall(line)
            for res in results:
                match = re.match(pattern_match, res)
                sum += int(match.group(1)) * int(match.group(2))
        print(sum)

    def part2(self, report_lines: list):
        pattern = re.compile("do\(\)|don't\(\)|mul\(\d+,\d+\)")
        pattern_match = r"mul\((\d+),(\d+)\)"
        sum = 0
        enabled = True
        for line in report_lines:
            results = pattern.findall(line)
            for res in results:
                if res == "do()":
                    enabled = True
                    continue
                elif res == "don't()":
                    enabled = False
                    continue

                if enabled:
                    match = re.match(pattern_match, res)
                    sum += int(match.group(1)) * int(match.group(2))
        print(sum)
    1

def main():
    solution = Day3()
    report_lines = solution.read_lines("2024/Day 3/input.txt")
    solution.part1(report_lines)
    solution.part2(report_lines)

main()