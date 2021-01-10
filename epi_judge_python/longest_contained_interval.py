from typing import List

from test_framework import generic_test

def get_subset(n, main_set):
    out = set([n])

    # left of n
    left = n - 1
    while left in main_set:
        out.add(left)
        left -= 1

    # right of n
    right = n + 1
    while right in main_set:
        out.add(right)
        right += 1

    return out

def longest_contained_range(A: List[int]) -> int:
    max_count = 0
    main_set = set(A)
    for n in A:
        if n in main_set:
            subset = get_subset(n, main_set)
            max_count = max(len(subset), max_count)
            main_set -= subset
    return max_count


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
