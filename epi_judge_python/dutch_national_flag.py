import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # O(n) time
    # O(1) time
    B = list(A)
    pivot = A[pivot_index]
    bottom = 0
    middle = 0
    bigger = len(A) - 1

    while middle <= bigger:
        if A[middle] < pivot:
            A[bottom], A[middle] = A[middle], A[bottom]
            bottom += 1
            middle +=1
        elif A[middle] == pivot:
            middle += 1
        elif A[middle] > pivot:
            A[bigger], A[middle] = A[middle], A[bigger]
            bigger -= 1

    return B

    # O(n) time
    # O(1) space
    # one pass, send to beg < index and to len -1 > index
    #pivot = A[pivot_index]
    #smaller = 0
    #for i in range(len(A)):
    #    if A[i] < pivot:
    #        A[i], A[smaller] = A[smaller], A[i]
    #        smaller += 1
    #bigger = len(A) - 1
    #for i in reversed(range(len(A))):
    #    if A[i] < pivot: 
    #        break
    #    elif A[i] > pivot:
    #        A[i], A[bigger] = A[bigger], A[i]
    #        bigger -= 1
    #return A


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
