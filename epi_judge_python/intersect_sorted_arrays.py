from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    idx_a, idx_b = 0, 0
    intersections = []
    while idx_a < len(A) and idx_b < len(B):
        if A[idx_a] == B[idx_b]:
            if not intersections or intersections[-1] != A[idx_a]:
                intersections.append(A[idx_a])
            idx_a += 1
            idx_b += 1
        elif A[idx_a] > B[idx_b]:
            idx_b += 1
        elif A[idx_a] < B[idx_b]:
            idx_a += 1

    return intersections


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
