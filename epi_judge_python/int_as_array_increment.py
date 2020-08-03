from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    carry = 1
    for i in reversed(range(len(A))):
        addition = A[i] + carry
        if addition >= 10:
            carry = 1
            addition  %= 10
        else:
            carry = 0

        A[i] = addition

    if carry:
        A[0] = carry
        A.append(0)
        
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
