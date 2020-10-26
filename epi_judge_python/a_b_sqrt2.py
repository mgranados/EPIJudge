from typing import List

from test_framework import generic_test
import bintrees
import math

class Number:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.val = a + b * math.sqrt(2)

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
    # Initial 
    candidates = bintrees.RBTree([(Number(0,0), None)])

    result = []
    while len(result) < k:
        next_smallest = candidates.pop_min()[0]
        result.append(next_smallest.val)

        candidates[Number(next_smallest.a + 1, next_smallest.b)] = None
        candidates[Number(next_smallest.a, next_smallest.b + 1)] = None

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('a_b_sqrt2.py', 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
