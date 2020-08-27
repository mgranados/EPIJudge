from test_framework import generic_test
from functools import lru_cache

@lru_cache()
def traverse_matrix(x, y):
    if x == 0 or y == 0:
        return 1

    up = traverse_matrix(x, y - 1)
    down = traverse_matrix(x - 1, y)
    return up + down

def number_of_ways(n: int, m: int) -> int:
    return traverse_matrix(n - 1, m - 1)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
