from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from collections import deque

def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    # 2 queues
    parents = deque()
    children = deque()
    result =  []
    
    # push node to parents
    if tree:
        parents.append(tree)

    # pop from parents until done, push to result
    parentList = []
    while parents: # popleft will return something
        #pop and get children
        rooty = parents.popleft()
        if rooty.left:
            children.append(rooty.left)
        if rooty.right:
            children.append(rooty.right)

        parentList.append(rooty.data)

        if not parents: # reviewed all parents 
            result.append(parentList)
            parentList = []
            # invert lists
            children, parents = parents, children

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
