from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    #final of A is m + n -1
    end_a = m + n - 1
    idx_a = m - 1
    idx_b = n - 1
    # iterate and compare a and b 
    while idx_a >= 0 or idx_b >= 0:
        if idx_a < 0:
            A[end_a] = B[idx_b]
            idx_b  -= 1
        elif idx_b < 0:
            A[end_a] = A[idx_a]
            idx_a -= 1
        elif B[idx_b] > A[idx_a]:
            A[end_a] = B[idx_b]
            idx_b -= 1
        else:
            A[end_a] = A[idx_a]
            idx_a -= 1
        end_a -= 1

        
    return A


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
