from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:

    def help_simmetry(t0, t1):
        if not t0 and not t1:
            return True

        if (t0 and not t1) or (t1 and not t0) or (t0.data != t1.data):
            return False

        return help_simmetry(t0.left, t1.right) and help_simmetry(t0.right, t1.left)

    if not tree:
        return True
    # only root
    return help_simmetry(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
