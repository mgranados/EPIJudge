from typing import List

from test_framework import generic_test, test_utils


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    def add_to_set(initial, so_far):
        if initial == len(input_set):
            power_set.append(so_far)
            return
        add_to_set(initial + 1, so_far)
        add_to_set(initial + 1, so_far + [input_set[initial]])

    power_set = []
    add_to_set(0, [])
    return power_set


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
