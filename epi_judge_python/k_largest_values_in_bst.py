from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils

def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    largest = []
    def aux_largest(node):
        if node:
            aux_largest(node.right)
            if len(largest) < k:
                largest.append(node.data)
            else:
                return
            aux_largest(node.left)
        else:
            return
        
    aux_largest(tree)

    return largest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
