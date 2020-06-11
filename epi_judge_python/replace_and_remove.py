import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    # -> look for total_b and remove
    num_b = 0
    num_a = 0
    for i in range(size):
        if s[i] == 'a':
            num_a += 1

        if s[i] == 'b':
            num_b += 1
            s[i] = ''

        elif num_b > 0:
           # swap
            s[i - num_b], s[i] = s[i], ''
            
    # -> send (num of a to right) look for a and insert dd
    final = size - num_b + num_a

    for j in reversed(range(size - num_b)):
        if s[j] == 'a':
            # send num a to right but 'd'
            s[j + num_a], s[j + num_a -1], = 'd', 'd'
            num_a -= 1
        else:
            s[j + num_a], s[j] = s[j], s[j + num_a]

    return final


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
