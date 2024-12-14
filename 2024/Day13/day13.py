class Day13:

    CACHE = {}

    def parse_input(self, filepath: str) -> list:
        lines = [line.rstrip() for line in open(filepath, 'r')]
        parsed_inputs = []
        inputs = {}
        for line in lines:
            parsed = line.split(":")
            if parsed[0]:
                coordinates = parsed[1].split(",")
                if parsed[0] == 'Button A':
                    inputs['A'] = (int(coordinates[0].split("+")[1]), int(coordinates[1].split("+")[1]))
                elif parsed[0] == 'Button B':
                    inputs['B'] = (int(coordinates[0].split("+")[1]), int(coordinates[1].split("+")[1]))
                elif parsed[0] == 'Prize':
                    inputs['Prize'] = (int(coordinates[0].split("=")[1]), int(coordinates[1].split("=")[1]))
                    parsed_inputs.append(inputs)
            else:
                inputs = {}

        return parsed_inputs

    def solve(self, machines, part2 = False):
        tokens = 0
        add = 10000000000000 if part2 else 0
        for machine in machines:
            x1 = machine['A'][0]
            y1 = machine['A'][1]
            x2 = machine['B'][0]
            y2 = machine['B'][1]

            prize_x = machine['Prize'][0] + add
            prize_y = machine['Prize'][1] + add
            a = (prize_x * y2 - prize_y * x2) / (x1 * y2 - y1 * x2)
            b = (prize_y * x1 - prize_x * y1) / (x1 * y2 - y1 * x2)
            if a == int(a) and b == int(b):
                tokens += int(3 * a + b)

        print(tokens)
    
def main():
    solution = Day13()
    machine = solution.parse_input("2024/Day13/input.txt")
    solution.solve(machine)
    solution.solve(machine, part2=True)

main()