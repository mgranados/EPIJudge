from typing import List

from test_framework import generic_test
import math

def find_nearest_repetition(paragraph: List[str]) -> int:
    # traverse O(n)
    # space O(d) distinct entries
    last_idx = {}
    min_dist = math.inf
    for idx, word in enumerate(paragraph):
        if word in last_idx:
            if idx - last_idx[word] < min_dist:
                min_dist = idx - last_idx[word] 
        last_idx[word] = idx
        

    return min_dist if min_dist != math.inf else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
