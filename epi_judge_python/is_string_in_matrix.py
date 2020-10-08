from typing import List
import functools

from test_framework import generic_test


def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    # receives coord offset 
    @functools.lru_cache(None)
    def is_pattern_helper(x, y, offset):
        if len(pattern) == offset:
            return True

        if (not (0 <= x < len(grid) and 0 <= y < len(grid[x])) or grid[x][y] !=
                pattern[offset]):
            return False

        for t in ((x-1, y), (x+1,y), (x,y-1), (x, y+1)):
            if is_pattern_helper(t[0], t[1], offset + 1):
                return True
        return False

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if is_pattern_helper(i, j, offset=0):
                return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
