from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int) -> None:
        self._list = [0] * capacity
        self._size = 0
        self._head = 0
        self._tail = 0
        return

    def enqueue(self, x: int) -> None:
        if self._tail == len(self._list):
            old = len(self._list)
            self._list = self._list[self._head:]
            self._list += [0] * old
            self._tail = self._tail - self._head
            self._head = 0

        self._list[self._tail] = x
        self._tail += 1
        self._size += 1
        return

    def dequeue(self) -> int:
        self._size -= 1
        to_dequeue = self._list[self._head]
        self._head += 1
        return to_dequeue

    def size(self) -> int:
        return self._size


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
