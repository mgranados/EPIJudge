import collections
import functools
from typing import List
from functools import lru_cache

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))

def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    @lru_cache(None)
    def get_clocks(idx, cap):
        if idx < 0:
            return 0

        if cap >= items[idx].weight:
            with_this = items[idx].value + get_clocks(idx-1, cap - items[idx].weight)
        else:
            with_this = 0

        prev = get_clocks(idx-1, cap)
        return max(prev, with_this)


    return get_clocks(len(items) - 1, capacity)


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
