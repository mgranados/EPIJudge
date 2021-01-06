from typing import List
import heapq

from test_framework import generic_test, test_utils


def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    if k == 0:
        return []

    helper_heap = []
    heapq.heappush(helper_heap, (-A[0], 0))
    results = []
    for _ in range(k):
        helper_idx = helper_heap[0][1]
        results.append(-heapq.heappop(helper_heap)[0])

        left = 2 * helper_idx + 1
        if left < len(A):
            heapq.heappush(helper_heap, (-A[left], left))
        right = 2 * helper_idx + 2
        if right < len(A):
            heapq.heappush(helper_heap, (-A[right], right))

    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
