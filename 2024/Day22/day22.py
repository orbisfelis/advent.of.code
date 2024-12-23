from collections import deque

class Day22:

    def parse_input(self, filepath: str):
        return list(map(int, [line.rstrip() for line in open(filepath, 'r')]))

    def mix_numbers(self, a, b):
        return a ^ b
    
    def prune_number(self, a):
        return a % 16777216
    
    def step_1(self, a):
        b = a * 64
        res = self.mix_numbers(a, b)
        return self.prune_number(res)
    
    def step_2(self, a):
        b = a // 32
        res = self.mix_numbers(a, b)
        return self.prune_number(res)
    
    def step_3(self, a):
        b = a * 2048
        res = self.mix_numbers(a, b)
        return self.prune_number(res)

    def part1(self, inputs, threshold = 10):
        results = dict()
        for input in inputs:
            prices = dict()
            changes = dict()
            res = input
            iteration = 0
            while iteration != threshold:
                last_digit = res % 10
                res = self.step_1(res)
                res = self.step_2(res)
                res = self.step_3(res)
                new_last_digit = res % 10
                changes[res] = (last_digit, new_last_digit - last_digit)
                iteration += 1
            results[input] = changes
        print(results)
        print([res.values() for res in results.values()])

def main():
    solution = Day22()
    inputs = solution.parse_input("2024/Day22/test_input.txt")
    threshold = 10
    solution.part1(inputs, threshold)

main()