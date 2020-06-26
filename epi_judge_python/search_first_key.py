from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    low = 0
    up = len(A) - 1
    while low <= up:
        med = low + (up - low) // 2
        if A[med] < k:
            low = med + 1
        elif A[med] == k:
            if med > 0 and A[med - 1] == k:
                up = med - 1
            else:
                return med
        else:
            up = med - 1
        # not seen
    return -1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
