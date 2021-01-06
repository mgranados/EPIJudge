from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    result = [0]
    sign = ''

    if num1[0] == '-':
        num1.remove('-')
        sign = '-'

    if num2[0] == '-':
        if sign == '-':
            sign = ''
        num2.remove('-')

    carry = 0
    for i in range(len(num2) - 1, -1, -1):
        // if carry append and reset
        for j in range(len(num1) - 1, -1, -1):
            idx_start = len(num1) - 1 - j
            partial = num1[j] * num2[i] + carry
            digit = partial % 10
            carry = partial // 10
            result[idx_start] += digit
            if result[idx_start] > 9:
                carry += 1
            if idx_start > len(result) - 1:
                result.append(0)



    if sign == '-':
        result.append(sign)

    result.reverse()
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
