from collections import Counter, defaultdict

class Day11:

    def parse_input(self, filepath: str) -> list:
        return list(map(int, [line.rstrip().split(" ") for line in open(filepath, 'r')][0]))
    
    '''
    RESULT_MAP = {}

    def old_rule_check(self, stone: int):
        # Part of Brute force part 1 solution.
        if stone in self.RESULT_MAP:
            pass
        elif stone == 0:
            self.RESULT_MAP[stone] = (1, )
        elif len(str(stone)) % 2 == 0:
            self.RESULT_MAP[stone] = int(str(stone)[:len(str(stone))//2]), int(str(stone)[len(str(stone))//2:])
        else:
            self.RESULT_MAP[stone] = (stone * 2024, )
        return self.RESULT_MAP[stone]
    
    def old_part1(self, stones: list, blinks: int = 25):
        # Brute force ok until 36-37 blinks, after that => pain.
        for _ in range(blinks):
            updated_stones = []
            for stone in stones:
                numbers = self.old_rule_check(stone)
                for number in numbers:
                    updated_stones.append(number)
            stones = updated_stones
        print(len(updated_stones))
    '''

    def blink(self, counts: Counter):
        updated_counts = defaultdict(int)
        for stone, count in counts.items():
            if stone == 0:
                updated_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                s = str(stone)
                s1, s2 = int(s[:len(s) // 2]), int(s[len(s) // 2:])
                updated_counts[s1] += count
                updated_counts[s2] += count
            else:
                updated_counts[stone * 2024] += count
        return updated_counts

    def solution(self, stones: list, blinks: int = 25):
        counts = Counter(stones)
        for _ in range(blinks):
            counts = self.blink(counts)
        return sum(counts.values())
    
    def part1(self, stones: list):
        print(self.solution(stones, 25))
    
    def part2(self, stones: list):
        print(self.solution(stones, 75))

def main():
    solution = Day11()
    stones = solution.parse_input("2024/Day11/input.txt")
    solution.part1(stones)
    solution.part2(stones)

main()