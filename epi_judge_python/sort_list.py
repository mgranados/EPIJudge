from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from sorted_lists_merge import merge_two_sorted_lists


def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    if L is None or L.next is None:
        return L
    pre_slow = None
    slow = L
    fast = L

    while fast and fast.next:
        pre_slow = slow
        fast = fast.next.next
        slow = slow.next

    if pre_slow:
        pre_slow.next = None

    return merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(slow)) 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
