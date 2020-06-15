from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    # get a sublist
    # get subhead of the reversing list
    # dummy head
    dummy_head = subhead = ListNode(0, L)
    # algoritmo volteo
    for _ in range(start - 1):
        subhead = subhead.next

    # ese iter es el inicio y siempre se ira al final
    sublist_iterator = subhead.next
    # un iter al inicio
    for _ in range(finish - start):
        temp = sublist_iterator.next
        # un temp despues de ese iter
        sublist_iterator.next = temp.next
        temp.next = subhead.next
        subhead.next = temp

    return dummy_head.next





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
