from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:
    if not preorder_sequence:
        return None
    biggest = len(preorder_sequence)
    for i, value in enumerate(preorder_sequence):
        if value > preorder_sequence[0]:
            biggest = i
            break

    return BstNode(preorder_sequence[0],
                   rebuild_bst_from_preorder(preorder_sequence[1:biggest]),
                   rebuild_bst_from_preorder(preorder_sequence[biggest:]))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
