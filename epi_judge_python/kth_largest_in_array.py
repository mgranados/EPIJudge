from typing import List

from test_framework import generic_test
import random

def find_kth_largest(k: int, A: List[int]) -> int:
    def in_place(left, right, pivot):
        pivot_value = A[pivot]
        # let pivot wait to the right
        A[right], A[pivot] = A[pivot], A[right]
        new_pivot_idx = left
        for i in range(left, right):
            # Only for value bigger, if pivot is the biggest, nothing happens
            if A[i] > pivot_value:
                # If we see a value bigger we send it as left as possible
                # new_pivot_idx
                A[new_pivot_idx], A[i] = A[i], A[new_pivot_idx]
                # set the new pivot + 1
                new_pivot_idx +=1
        # once all bigger are in place
        # switch with np the right (original pivot)
        # if pivot was the biggest we simply place it to the left
        A[new_pivot_idx], A[right] = A[right], A[new_pivot_idx]
        return new_pivot_idx

    left, right = 0, len(A) - 1
    while left <= right:
        # Pick a random pivot
        pivot = random.randint(left, right)
        new_pivot = in_place(left, right, pivot)
        # new pivot around 
        if new_pivot == k - 1:
            return A[new_pivot]
        elif new_pivot > k -1:
            # there are more bigger numbers
            # cut the right (smaller numbers)
            right = new_pivot - 1
        else:
            # there are more smaller numbers [3, →2, 1, -2] k = 3(-1) > (np = 1)
            # cut the left (bigger numbers)
            left = new_pivot + 1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
