from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if L is None:
        return L
    odd = ListNode()
    even = ListNode()
    head_odd = odd
    head_even = even
    odd_count = False
    while L:
        # if odd send to other list
        if odd_count:
            odd.next = L
            odd = odd.next
        else:
            even.next = L
            even = even.next
        odd_count = not odd_count
        L = L.next

    odd.next = None
    even.next = None

    even.next = head_odd.next
    return head_even.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
