import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    if len(A) <= 1:
        return len(A)
    new_len = 1
    moving = 1
    while moving < len(A):
        if A[moving] > A [new_len - 1]:
            A[moving], A[new_len] = A[new_len], A[moving]
            new_len +=1
        moving += 1
    return new_len 


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
