from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    result = []
    if len(A) <= 1:
        return [A]

    def recursive_helper(index):
        if index == len(A) - 1: # we at the last one
            result.append(A.copy())
            return

        for i in range(index, len(A)): # [1, 2, 3]
            A[index], A[i] = A[i], A[index] # [2, 1, 3]
            recursive_helper(index + 1) # [2, *1*, 3]
            A[i], A[index] = A[index], A[i] # [1, 2, 3]

    recursive_helper(0)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
