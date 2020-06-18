from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import math

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
        
    def getDepth(node):
        if not node:
            return 0
        if abs(getDepth(node.left) - getDepth(node.right)) > 1:
            raise Exception('depth was too big')
        
        return 1 + max(getDepth(node.left), getDepth(node.right))

    try:
        depth = getDepth(tree) >= 0
    except:
        return False

    return depth

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
