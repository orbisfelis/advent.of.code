from heapq import heappush, heappop
from collections import Counter

def part1():
    heap1, heap2 = [], []
    sum = 0
    with open("2024/Day 1/input.txt", 'r') as file:
        lines = [line.rstrip() for line in file]
        for line in lines:
            coordinates = line.split("   ")
            heappush(heap1, int(coordinates[0]))
            heappush(heap2, int(coordinates[1]))
    while heap1 and heap2:
        sum += abs(heappop(heap1) - heappop(heap2))
    print(sum)

part1()

def part2():
    inputs1, inputs2 = [], []
    sum = 0
    with open("2024/Day 1/input.txt", 'r') as file:
        lines = [line.rstrip() for line in file]
        for line in lines:
            coordinates = line.split("   ")
            inputs1.append(int(coordinates[0]))
            inputs2.append(int(coordinates[1]))
        
        counts = Counter(inputs2)
        for coordinate in inputs1:
            sum += coordinate * counts.get(coordinate, 0)
        
    print(sum)

part2()