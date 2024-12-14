import re
import math
from copy import deepcopy

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

class Day14:

    def parse_input(self, filepath: str) -> list:
        robots = {}
        idx = 0
        lines = [line.rstrip() for line in open(filepath, 'r')]
        for line in lines:
            pattern = r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)"
            match = re.match(pattern, line)
            if match:
                p_y, p_x, v_y, v_x = map(int, match.groups())
                robots[idx] = {"p": (p_x, p_y), "v": (v_x, v_y)}
                idx += 1
        return robots

    def count_quadrants(self, robots, grid_x, grid_y):
        mid_x = grid_x // 2
        mid_y = grid_y // 2

        quadrant_counts = {'TOPLEFT': 0, 'TOPRIGHT': 0, 'BOTTOMLEFT': 0, 'BOTTOMRIGHT': 0}

        for robot_id, details in robots.items():
            position = details['p']
            if position[0] == mid_x or position[1] == mid_y: continue
            if position[0] < mid_x and position[1] < mid_y:
                quadrant_counts['TOPLEFT'] += 1
            elif position[0] < mid_x and position[1] > mid_y:
                quadrant_counts['TOPRIGHT'] += 1
            elif position[0] > mid_x and position[1] < mid_y:
                quadrant_counts['BOTTOMLEFT'] += 1
            elif position[0] > mid_x and position[1] > mid_y:
                quadrant_counts['BOTTOMRIGHT'] += 1
        
        safety_score = math.prod(quadrant_counts.values())
        return safety_score, quadrant_counts
    
    def move_robots(self, robots, grid_x, grid_y):
        for robot_id, details in robots.items():
            current_position = details['p']
            velocity = details['v']
            new_x = current_position[0] + velocity[0]
            new_y = current_position[1] + velocity[1]
            if new_x >= grid_x:
                new_x = new_x - grid_x
            elif new_x < 0:
                new_x = grid_x + new_x
            if new_y >= grid_y:
                new_y = new_y - grid_y
            elif new_y < 0:
                new_y = grid_y + new_y
            robots[robot_id] = {'p': (new_x, new_y), 'v': velocity}
        return robots
    
    def render_robot_locations(self, robots, grid_x, grid_y):
        data = []
        for robot_id, details in robots.items():
            data.append(details['p'])
        data = np.array(data)
        x, y = data.T
        plt.scatter(x, y, color="tab:green")
        plt.show()

    def solutions(self, robots, grid_x, grid_y, seconds, part2=False):
        updated_positions = deepcopy(robots)
        for _ in range(1, seconds+1):
            updated_positions = self.move_robots(updated_positions, grid_x, grid_y)
            if part2:
                '''
                    Safety factor is usually low, look for a quadrant with lots of nodes.
                    Using factor of 250 nodes (i.e. 50%+)
                    Render using matplotlib to confirm.
                '''
                safety_factor, quadrant_counts = self.count_quadrants(updated_positions, grid_x, grid_y)
                if any((lambda x: x for x in quadrant_counts.values() if x > 250)):
                    print(f"A Christmas Tree materializes! Seconds elapsed: {_}, Quadrant counts: {quadrant_counts}")
                    self.render_robot_locations(updated_positions, grid_x, grid_y)
        if not part2:
            print(updated_positions)
            print(self.count_quadrants(updated_positions, grid_x, grid_y)[0])


def main():
    solution = Day14()
    '''
    file = "test_input.txt"
    grid_x = 7
    grid_y = 11
    seconds = 100
    '''
    file = "input.txt"
    grid_x = 103
    grid_y = 101
    seconds = 100
    inputs = solution.parse_input(f"2024/Day14/{file}")
    solution.solutions(inputs, grid_x, grid_y, seconds)
    
    seconds = 10000
    solution.solutions(inputs, grid_x, grid_y, seconds, part2=True)

main()