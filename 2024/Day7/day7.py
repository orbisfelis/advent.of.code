class Day7:

    def parse_input(self, filepath: str) -> list:
        return [(int(inputs[0]), list(map(int, inputs[1].strip().split(' ')))) for inputs in [line.rstrip().split(":") for line in open(filepath, 'r')]]

    def calculate(self, nums, index, current_sum, target):
        if index == len(nums):
            return target if current_sum == target else 0
        else:
            if current_sum > target:
                return 0
            else:
                return self.calculate(nums, index+1, current_sum + nums[index], target) or \
                       self.calculate(nums, index+1, current_sum * nums[index], target)
    
    def solve_sum(self, inputs, method):
        sum = 0
        for input in inputs:
            res = method(input[1], 0, 0, input[0])
            sum += res
        return sum

    def part1(self, inputs):
        print(self.solve_sum(inputs, self.calculate))
    
    def concatenate(self, num1, num2):
        return int(str(num1) + str(num2))
    
    def calculate2(self, nums, index, current_sum, target):
        if index == len(nums):
            return target if current_sum == target else 0
        else:
            if current_sum > target:
                return 0
            else:
                return self.calculate2(nums, index+1, current_sum + nums[index], target) or \
                       self.calculate2(nums, index+1, current_sum * nums[index], target) or \
                       self.calculate2(nums, index+1, self.concatenate(current_sum, nums[index]), target)
    
    def part2(self, inputs):
        print(self.solve_sum(inputs, self.calculate2))

def main():
    solution = Day7()
    inputs = solution.parse_input("2024/Day7/input.txt")
    solution.part1(inputs)
    solution.part2(inputs)

main()