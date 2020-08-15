from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    # binary search
    # if mid > right 
    # min must be there because a cycle was done
    # else
    # 546, 103, 442, 455, 466, 477
    right = len(A) - 1
    left = 0

    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[right]:
            left = mid + 1
        else:
            right = mid


    return right


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
