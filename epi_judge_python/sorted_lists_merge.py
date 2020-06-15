from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:

    if L1 and not L2:
        return L1
    if L2 and not L1:
        return L2
    if not L2 and not L1:
        return None
    
    if L1.data < L2.data:
        head = L1
        tail = ListNode(0, head)
        L1 = L1.next
    else:
        head = L2
        tail = ListNode(0, head)
        L2 = L2.next

    while L1 or L2:
        if not L1:
            head.next = L2
            break

        if not L2:
            head.next = L1
            break

        if L1.data < L2.data:
            head.next = L1
            L1 = L1.next
        else:
            head.next = L2
            L2 = L2.next

        head = head.next

    return tail.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
