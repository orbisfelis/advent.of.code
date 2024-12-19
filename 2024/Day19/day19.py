from functools import cache

class Day19:

    def parse_input(self, filepath: str) -> tuple:
        patterns, designs = [], []
        lines = [line.rstrip() for line in open(filepath, 'r')]
        patterns = [line.strip() for line in lines[0].split(",")]
        for design in lines[2:]:
            designs.append(design)
        return tuple(patterns), designs
    
    @cache
    def count_combos(self, patterns, design):
        sum = 0
        for pattern in patterns:
            if design:
                if design.startswith(pattern):
                    sum += self.count_combos(patterns, design[len(pattern):])
            else:
                return 1
        return sum
    
    def solution(self, patterns: tuple, designs: list):
        combos = [self.count_combos(patterns, design) for design in designs]
        print(f"Part 1: {len([combo for combo in combos if combo])}")
        print(f"Part 2: {sum(combos)}")

def main():
    solution = Day19()
    patterns, designs = solution.parse_input("2024/Day19/input.txt")
    solution.solution(patterns, designs)

main()