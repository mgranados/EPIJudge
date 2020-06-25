from typing import List

from test_framework import generic_test
import heapq
from collections import namedtuple

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    TupleArray = namedtuple('TupleArray', ['value', 'index'])
    # heap with first of each array
    max_heap = []
    for idx, array in enumerate(sorted_arrays):
        if array:
            heapq.heappush(max_heap, TupleArray((-array[-1]), idx))
            array.pop() # pop(0) == O(n)

    # then peek heap and compare with parent list
    res = []
    while max_heap:
        # peek
        peeking = max_heap[0]
        # if comparing to empty list push value to res
        if not sorted_arrays[peeking.index]:
            res.append(-peeking.value)
            heapq.heappop(max_heap)
            continue
       
        # if list contains equal push directly to res
        if sorted_arrays[peeking.index][-1] == -peeking.value:
            res.append(-peeking.value)
            sorted_arrays[peeking.index].pop()
            continue

        if sorted_arrays[peeking.index][-1] < -peeking.value:
            popped = heapq.heappushpop(max_heap,
                                       TupleArray(-sorted_arrays[peeking.index][-1],
                                         peeking.index))
            res.append(-popped.value)
            sorted_arrays[peeking.index].pop()
            continue

    return res[::-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
