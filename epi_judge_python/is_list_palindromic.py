from list_node import ListNode
from test_framework import generic_test

def reverse_list(head):
    aux = ListNode(0)
    while head:
        aux.next, head.next, head = head, aux.next, head.next
    return aux.next


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    if not L:
        return True
    # keep one at head
    tail = L
    mid = L
    # go to the mid
    while tail and tail.next:
        mid = mid.next
        tail = tail.next.next

    # reverse from mid
    straight, reverse = L, reverse_list(mid)
    # compare head <> tail
    while straight and reverse:
        if straight.data != reverse.data:
            return False
        straight= straight.next
        reverse= reverse.next

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
