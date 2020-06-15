import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def has_cycle(head: ListNode) -> Optional[ListNode]:
    dummy_head  = ListNode(0, head)
    # advance 1 and 2
    normal = faster = head
    dummy_list = ListNode(0, None)

    while True:
        if faster is None or faster.next is None:
            return None # no cycle

        faster = faster.next
        faster = faster.next

        if faster is normal:
            dummy_list.next = normal
            break;

        normal = normal.next
        # where they match that's cycle.
        if normal is faster:
            dummy_list.next = normal
            break;

    cycle_head = dummy_list.next
    cycle = cycle_head.next
    count = 1
    while cycle is not cycle_head:
        count += 1
        cycle = cycle.next
           
    # keep moving 1 until back to that 
    plus_cycle = normal = head
    # move 1 and other len of cycle
    for _ in range(count):
        plus_cycle = plus_cycle.next

    # where they match that's head
    while plus_cycle is not normal:
        plus_cycle = plus_cycle.next
        normal = normal.next
        
    # then move both 1 
    return plus_cycle


@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError('Can\'t cycle empty list')
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError('Can\'t find a cycle start')
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure('Found a non-existing cycle')
    else:
        if result is None:
            raise TestFailure('Existing cycle was not found')
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    'Returned node does not belong to the cycle or is not the closest node to the head'
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            'Returned node does not belong to the cycle or is not the closest node to the head'
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_cyclic.py',
                                       'is_list_cyclic.tsv',
                                       has_cycle_wrapper))
