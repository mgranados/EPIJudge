from typing import Iterator, List

from test_framework import generic_test
import heapq

def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    result = []
    k_heap = []

    seq = iter(sequence)

    for i in range(k):
        heapq.heappush(k_heap, next(seq))

    for val in seq:
        result.append(heapq.heappushpop(k_heap, val))

    result.extend(heapq.nsmallest(k, k_heap))

    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
