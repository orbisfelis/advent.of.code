import itertools
from collections import defaultdict

class Day8:

    THE_MAP = None

    def parse_input(self, filepath: str) -> list:
        return [list(item) for item in [line.rstrip() for line in open(filepath, 'r')]]
    
    def generate_coordinate_map(self):
        coordinate_map = defaultdict(list)
        for idx_r, r in enumerate(self.THE_MAP):
            for idx_c, c in enumerate(r):
                key = self.THE_MAP[idx_r][idx_c]
                if key != '.':
                    coordinate_map[key].append((idx_r, idx_c))
        return coordinate_map

    def check_in_bounds(self, coordinates: tuple):
        R, C = len(self.THE_MAP), len(self.THE_MAP[0])
        if min(coordinates[0], coordinates[1]) < 0 or coordinates[0] >= R or coordinates[1] >= C:
            return False
        return True
    
    def get_antinodes(self, antena1_coord: tuple, antena2_coord: tuple):
        '''
            Use two coordinates first taking one as middle then other.
            Formula for finding middle: (m1, m2) = ((x1 + x2)/2, (y1 + y2)/2)
            Find one side (x1): (x1, y1) = (2*m1-x2, 2*m2-y2)
            Find other side (x2): (x2, y2) = (2*m1-x1, 2*m2-y1)

            e.g.
            a1: (1, 8); a2: (2, 5)
            anti_1 = ((2 * 1 - 2), (2 * 8 - 5)) = (0, 11)  -> within bounds
            anti_2 = ((2 * 2 - 1), (2 * 5 - 8)) = (3, 2) -> within bounds

            Only return if within bounds.
        '''
        antinode_1 = ((2 * antena1_coord[0] - antena2_coord[0]), (2 * antena1_coord[1] - antena2_coord[1]))
        antinode_2 = ((2 * antena2_coord[0] - antena1_coord[0]), (2 * antena2_coord[1] - antena1_coord[1]))

        results = []
        if self.check_in_bounds(antinode_1):
            results.append(antinode_1)
        if self.check_in_bounds(antinode_2):
            results.append(antinode_2)
        
        return results
    
    def get_all_antinodes(self, antena1_coord: tuple, antena2_coord: tuple):
        '''
            e.g.
            a1: (1, 8); a2: (2, 5)
            anti_1 = ((2 * 1 - 2), (2 * 8 - 5)) = (0, 11)  -> within bounds
            anti_2 = ((2 * 2 - 1), (2 * 5 - 8)) = (3, 2) -> within bounds

            anti_1_1 ((2 * 0 - 1), (2 * 11 - 8)) = (-1, 13) -> out of bounds
            anti_2_2 ((2 * 3 - 2), (2 * 2 - 5)) = (4, -1) -> out of bounds
        '''
        results = []
        
        # Keep going one direction until out of bounds. Append result to result set.
        curr_c_1 = antena1_coord
        curr_c_2 = antena2_coord
        while True:
            antinode_1 = ((2 * curr_c_1[0] - curr_c_2[0]), (2 * curr_c_1[1] - curr_c_2[1]))
            if not self.check_in_bounds(antinode_1):
                break
            results.append(antinode_1)
            curr_c_2 = curr_c_1
            curr_c_1 = antinode_1

        # Keep going in other direction until out of bounds
        curr_c_1 = antena1_coord
        curr_c_2 = antena2_coord
        while True:
            antinode_2 = ((2 * curr_c_2[0] - curr_c_1[0]), (2 * curr_c_2[1] - curr_c_1[1]))
            if not self.check_in_bounds(antinode_2):
                break
            results.append(antinode_2)
            curr_c_1 = curr_c_2
            curr_c_2 = antinode_2
        
        # We also have coordinates on both originating antenas.
        results.extend([antena1_coord, antena2_coord])
        return list(set(results))
    
    '''
        PART 1, PART 2 Solutions Below
    '''

    def get_results(self, coordinate_map: dict, method):
        all_antinode_coordinates = []
        for coordinates in coordinate_map.values():
            if len(coordinates) > 1:
                combinations = itertools.combinations(coordinates, 2)
                for nodes in combinations:
                    all_antinode_coordinates.extend(method(nodes[0], nodes[1]))
        return all_antinode_coordinates
    
    def part1(self, coordinate_map: dict):
        print(len(set(self.get_results(coordinate_map, self.get_antinodes))))
    
    def part2(self, coordinate_map: dict):
        print(len(set(self.get_results(coordinate_map, self.get_all_antinodes))))

def main():
    solution = Day8()
    map = solution.parse_input("2024/Day8/input.txt")
    solution.THE_MAP = map
    coordinate_map = solution.generate_coordinate_map()
    solution.part1(coordinate_map)
    solution.part2(coordinate_map)

main()