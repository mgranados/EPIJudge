from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    def helper(root, preorder):
        node = BinaryTreeNode(root)

        pivot = inorder.index(root)
        left = inorder[:pivot]
        right = inorder[pivot+1:]
        left_nodes = []
        right_nodes = []
        for val in preorder:
            if val in left:
                left_nodes.append(val)
            else:
                right_nodes.append(val)

        if left_nodes:
            node.left = helper(left_nodes[0], left_nodes[1:] )
        if right_nodes:
            node.right = helper(right_nodes[0], right_nodes[1:] )
        return node

    if not preorder or not inorder:
        return None

    return helper(preorder[0], preorder[1:])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
