import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))

# [122, false, 131, false] [129, false, 137, true] -> [131, true, 133, true] -> [136, true, 137, false]

def union_of_intervals(intervals: List[Interval]) -> List[Interval]:
    if not intervals:
        return []
    sorted_intervals = sorted(intervals, key=lambda interval:
                              (interval.left.val, not interval.left.is_closed))
    result = [sorted_intervals[0]]

    for interval in sorted_intervals:
        if (interval.left.val < result[-1].right.val or
                          (interval.left.val == result[-1].right.val and 
                           (interval.left.is_closed or
                            result[-1].right.is_closed))):
            if (interval.right.val > result[-1].right.val or
                    (interval.right.val == result[-1].right.val and
                     interval.right.is_closed)):
                result[-1] = Interval(result[-1].left, interval.right) 
        else:
            result.append(interval)

    return result


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intervals_union.py',
                                       'intervals_union.tsv',
                                       union_of_intervals_wrapper))
