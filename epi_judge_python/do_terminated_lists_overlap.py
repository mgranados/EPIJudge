import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    if not l0 or not l1:
        return None

    def list_len(list_to_test):
        count = 0
        while(list_to_test.next):
            count += 1
            list_to_test = list_to_test.next
        return count

    len0 = list_len(l0)
    len1 = list_len(l1)

    #save only diff

    if len0 > len1: 
        while len0 > len1 and l0.next:
            l0 = l0.next
            len0 -= 1
        
    elif len1 > len0:
        while len1 > len0 and l1.next:
            l1 = l1.next
            len1 -= 1
        
    while len1 > 0:
        if not l0 or not l1:
            return None

        if l0 == l1:
            return l0
        l0 = l0.next
        l1 = l1.next
        len1 -= 1

    return None


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
