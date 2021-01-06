import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A: List[int]) -> MinMax:
    if len(A) <= 1:
        return MinMax(A[0], A[0])

    max_max = A[0]
    min_min = A[0]
    a = 0
    b = 1

    while a < len(A) and b < len(A):
        if A[a] < A[b]:
            max_max = max(max_max, A[b])
            min_min = min(min_min, A[a])
        else:
            max_max = max(max_max, A[a])
            min_min = min(min_min, A[b])
        a += 2
        b += 2

    if len(A) % 2:
            max_max = max(max_max, A[-1])
            min_min = min(min_min, A[-1])

    return MinMax(min_min, max_max)


def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_min_max_in_array.py',
                                       'search_for_min_max_in_array.tsv',
                                       find_min_max,
                                       res_printer=res_printer))
