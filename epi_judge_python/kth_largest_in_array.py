from typing import List

from test_framework import generic_test
import random

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    def partition(left, right, pivot):
        pivot_value = A[pivot]
        new_pivot = left
        A[pivot], A[right] = A[right], A[pivot]
        for i in range(left, right):
            if A[i] > pivot_value:
                A[i], A[new_pivot] = A[new_pivot], A[i]
                new_pivot += 1
        A[right], A[new_pivot] = A[new_pivot], A[right]
        return new_pivot

    left, right = 0, len(A) - 1
    while left <= right:
        # Random pivot
        pivot = random.randint(left, right)
        # pivot around 
        new = partition(left, right, pivot)
        if new == k - 1:
            return A[new]
        elif new > k -1:
            right = new - 1
        else:
            left = new + 1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
