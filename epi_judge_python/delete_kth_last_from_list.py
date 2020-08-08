from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    head = L
    fwd = L
    count = 0;

    while count < k:
        fwd = fwd.next
        count +=1

    prev = ListNode()
    while fwd:
        # aux para saber el anterior y brincarlo
        prev = head
        head = head.next
        fwd = fwd.next

    if head == L:
        L = head.next
    else:
        prev.next = head.next

    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
