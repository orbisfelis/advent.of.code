import networkx as nx
from collections import defaultdict
from typing import Dict, List

class Day23:

    def parse_input(self, filepath: str) -> List[List]:
        return [line.rstrip().split("-") for line in open(filepath, "r")]

    def build_adjacency_list(self, edges: List[List]) -> Dict[str, List]:
        adj_list = defaultdict(list)
        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)
        return adj_list
    
    def build_possible_triples(self, adj_list: Dict[str, List]) -> List:
        possibles = list()
        for node, children in adj_list.items():
            for child in children:
                r = children.index(child) + 1
                while r < len(children):
                    if child in adj_list[children[r]]:
                        triple = sorted([node, child, children[r]])
                        if triple not in possibles:
                            possibles.append(triple)
                    r += 1
        return sorted(possibles)
    
    def part1(self, adj_list: Dict[str, List]) -> None:
        possibles = self.build_possible_triples(adj_list)
        results = []
        for possible in possibles:
            for child in possible:
                if child.startswith('t'):
                    results.append(possible)
                    break
        print(len(results))
    
    def part2(self, edges: List[List]) -> None:
        '''
            Is it cheating to use a graph library for part2?
            Find maximum cliques within graph.
        '''
        graph = nx.Graph()
        graph.add_edges_from(edges)
        max_cliques = list(nx.find_cliques(graph))
        password_l = sorted(max(max_cliques, key=len))
        password = ",".join(password_l)
        print(password)

    
def main():
    solution = Day23()
    inputs = solution.parse_input("2024/Day23/input.txt")
    adj_list = solution.build_adjacency_list(inputs)
    solution.part1(adj_list)
    solution.part2(inputs)

main()