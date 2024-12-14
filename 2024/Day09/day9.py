class Day9:

    def parse_input(self, filepath: str) -> list:
        return [int(c) for c in [line.rstrip() for line in open(filepath, 'r')][0]]
    
    def create_disk_layout(self, input: list):
        disk_layout = []
        file_sizes = {}
        space_sizes = []
        current_id = 0
        is_file = True
        for i in input:
            curr_id = len(disk_layout)
            for _ in range(i):
                if is_file:
                    disk_layout.append(current_id)
                    file_sizes[current_id] = file_sizes.get(current_id, 0) + 1
                else:
                    disk_layout.append(".")
            if not is_file:
                space_sizes.append((i, curr_id,))
            is_file = not is_file
            if is_file:
                current_id += 1
        return disk_layout, file_sizes, space_sizes

    def calculate_checksum(self, disk_layout: list):
        sum = 0
        for idx, i in enumerate(disk_layout):
            if i == ".":
                continue
            sum += idx * i
        return sum

    '''
        PART1, PART2 Solutions Below
    '''
    def part1(self, disk_layout: list):
        start_ptr = 0
        end_ptr = len(disk_layout) - 1
        while start_ptr < end_ptr:
            if disk_layout[start_ptr] != ".":
                start_ptr += 1
            else:
                if disk_layout[end_ptr] != ".":
                    disk_layout[start_ptr] = disk_layout[end_ptr]
                    disk_layout[end_ptr] = "."
                    end_ptr -= 1
                else:
                    end_ptr -= 1
        print(self.calculate_checksum(disk_layout))
    
    def part2(self, disk_layout: list, file_sizes: dict, space_sizes: list):
        end_ptr = len(disk_layout) - 1
        while end_ptr >= 0:
            if disk_layout[end_ptr] != ".":
                item = disk_layout[end_ptr]
                size = file_sizes[item]
                updated = False
                for idx, space in enumerate(space_sizes):
                    avail_size, start_idx = space
                    if start_idx > end_ptr:
                        break
                    if size <= avail_size:
                        for idx_s in range(size):
                            disk_layout[start_idx + idx_s] = item
                            disk_layout[end_ptr] = "."
                            end_ptr -= 1
                        space_sizes[idx] = (avail_size - size, start_idx + size)
                        updated = True
                        break
                if not updated:
                    curr_item = disk_layout[end_ptr]
                    while curr_item == disk_layout[end_ptr]:
                        end_ptr -= 1
            else:
                end_ptr -= 1
            
        print(self.calculate_checksum(disk_layout))

def main():
    solution = Day9()
    disk_input = solution.parse_input("2024/Day9/input.txt")
    disk_layout, file_sizes, space_sizes = solution.create_disk_layout(disk_input)
    solution.part1(disk_layout)
    solution.part2(disk_layout, file_sizes, space_sizes)

main()
    