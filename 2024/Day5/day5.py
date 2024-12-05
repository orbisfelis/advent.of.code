from functools import cmp_to_key

class Day5:

    def read_lines(self, filepath: str) -> list:
        return [line.rstrip() for line in open(filepath, 'r')]

    def check_valid(self, rules: dict, orders: list):
        for idx, page in enumerate(orders):
            for after_page in orders[idx+1:]:
                if page in rules[after_page]:
                    return False
        return True

    def sort_via_rules(self, rules: dict, orders: list):
        def compare(a: int, b: int) -> int:
            return 1 if a in rules[b] else -1
        ordered_list = sorted(orders, key=cmp_to_key(compare))
        return ordered_list
    
    def part1(self, rules: dict, print_order: list):
        sum = 0
        for orders in print_order:
            if self.check_valid(rules, orders):
                middle_index = (len(orders) - 1)//2
                sum += orders[middle_index]
        print(sum)

    def part2(self, rules: dict, print_order: list):
        sum = 0
        for orders in print_order:
            if not self.check_valid(rules, orders):
                sorted = self.sort_via_rules(rules, orders)
                middle_index = (len(sorted) - 1)//2
                sum += sorted[middle_index]
        print(sum)

def main():
    solution = Day5()
    file = solution.read_lines("2024/Day5/test_input.txt")
    rules = {}
    print_order = []
    for line in file:
        if '|' in line:
            src, dst = map(int, line.split('|'))
            if src not in rules:
                rules[src] = []
            if dst not in rules:
                rules[dst] = []
            rules[src].append(dst)
        if line == '':
            continue
        if "," in line:
            print_order.append(list(map(int, line.split(','))))
    solution.part1(rules, print_order)
    solution.part2(rules, print_order)

main()