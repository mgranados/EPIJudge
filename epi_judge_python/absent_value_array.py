from typing import Iterator
import math

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from itertools import tee

def find_missing_element(stream: Iterator[int]) -> int:
    curr_stream, iter_copy = tee(stream)
    # get mins and max
    min = math.inf
    max = -math.inf
    for value in curr_stream:
        if value < min:
            min = value
        if value > max:
            max = value

    flag = True

    while flag:
        curr_stream, iter_copy = tee(iter_copy) 
        pivot = (max - min) // 2

        min_left, max_left, count_left = min, pivot, 0
        len_left = (max_left - min_left) + 1
        min_right, max_right, count_right = pivot + 1, max, 0
        len_right = max_right - min_right

        count = 0
        for current in curr_stream:
            count += 1
            if current >= max_left:
                count_right += 1
            else:
                count_left += 1

        if min_left == max_left or min_right == max_right:
            if count_left == 0:
                print(min_left)
                return min_left
            if count_right == 0:
                print(min_right)
                return min_right
            flag = False

        # move min max
        if count_right < len_left:
            min = min_left
            max = max_left
        else:
            min = min_right
            max = max_right

    return 'oops'

def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure('{} appears in stream'.format(res))
    except ValueError:
        raise TestFailure('Unexpected no missing element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('absent_value_array.py',
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
