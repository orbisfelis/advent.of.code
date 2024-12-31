from operator import add

class Day25:
    
    def parse_input(self, filepath: str):
        keys, locks = [], []
        key_or_lock = []

        def add_key_or_lock(key_or_lock):
            if key_or_lock[0] == '#####':
                height_counts = [0] * 5
                for i in range(1, len(key_or_lock)):
                    for j in range(0, len(key_or_lock[i])):
                        height_counts[j] += 1 if key_or_lock[i][j] == '#' else 0
                locks.append(height_counts)
            else:
                height_counts = [0] * 5
                for i in range(0, len(key_or_lock)-1):
                    for j in range(0, len(key_or_lock[i])):
                        height_counts[j] += 1 if key_or_lock[i][j] == '#' else 0
                keys.append(height_counts)

        for line in open(filepath, 'r'):
            line = line.rstrip()
            if line != '':
                key_or_lock.append(line)
            else:
                add_key_or_lock(key_or_lock)
                key_or_lock = []

        add_key_or_lock(key_or_lock)
        return keys, locks
    
    def part1(self, keys, locks):
        unique_pairs = 0
        for key in keys:
            for lock in locks:
                check = list(map(add, key, lock))
                if not any([item > 5 for item in check]):
                    unique_pairs += 1
        print(unique_pairs)

def main():
    solution = Day25()
    keys, locks = solution.parse_input("2024/Day25/input.txt")
    solution.part1(keys, locks)

main()