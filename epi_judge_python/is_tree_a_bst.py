from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import math

def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    def in_range(tree, low=-math.inf, high=math.inf):
        if not tree:
            return True
        elif not low <= tree.data <= high:
            return False
        return in_range(tree.left, low, tree.data) and in_range(tree.right,
                                                                tree.data,
                                                                high)
    return in_range(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
