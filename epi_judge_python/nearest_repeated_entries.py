from typing import List

from test_framework import generic_test
import math

def find_nearest_repetition(paragraph: List[str]) -> int:
    min_dist = math.inf;
    counts = {}
    for index, char in enumerate(paragraph):
        if char in counts:
            curr_dist = index - counts[char]
            min_dist = curr_dist if curr_dist < min_dist else min_dist
            counts[char] = index
        else:
            counts[char] = index

    return -1 if min_dist == math.inf else min_dist


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
