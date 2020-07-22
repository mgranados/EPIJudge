from typing import List

from test_framework import generic_test

def has_three_sum(A: List[int], t: int) -> bool:
    def two_sum(B, s):
        seted = set(B)
        for n in B:
            if s - n in seted:
                return True
        return False

    for num in A:
        if two_sum(A, t - num):
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
