from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import math
from collections import namedtuple

NodeInfo = namedtuple('NodeInfo', ['height', 'balanced'])

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    #def get_depth(node):
    #    if not node:
    #        return 0
    #    if abs(get_depth(node.left) - get_depth(node.right)) > 1:
    #        raise Exception('depth was too big')
    #    return 1 + max(get_depth(node.left), get_depth(node.right))

    #try:
    #    depth = get_depth(tree) >= 0
    #except:
    #    return False
    #return depth
    def get_node_info(node):
        if not node:
            return NodeInfo(-1, True)

        left = get_node_info(node.left)
        if not left.balanced:
            return NodeInfo(-99999, False)

        right = get_node_info(node.right)
        if not right.balanced:
            return NodeInfo(-99999, False)

        height = max(left.height, right.height) + 1
        balanced = abs(left.height - right.height) < 2

        return NodeInfo(height, balanced)

    return get_node_info(tree).balanced





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
