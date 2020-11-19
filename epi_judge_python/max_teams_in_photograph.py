import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    def __init__(self) -> None:
        self.edges: List[GraphVertex] = []
        # Set max_distance = 0 to indicate unvisitied vertex.
        self.max_distance = 0


def find_largest_number_teams(graph: List[GraphVertex]) -> int:
    def dfs(node):
        biggest_dist = 0
        for edge in node.edges:
            if edge.max_distance == 0:
                edge.max_distance = dfs(edge)
            biggest_dist = max(biggest_dist, edge.max_distance)

        return biggest_dist + 1

    biggest_child = 0
    for node in graph:
        if node.max_distance == 0:
            node.max_distance = dfs(node)
        biggest_child = max(biggest_child, node.max_distance)

    return biggest_child


@enable_executor_hook
def find_largest_number_teams_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(find_largest_number_teams, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_teams_in_photograph.py',
                                       'max_teams_in_photograph.tsv',
                                       find_largest_number_teams_wrapper))
