# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CustomTree:
    def __init__(self, treeNode: TreeNode):
        self.root = treeNode
        self.root.depth = 0
        self.root.parent = None
        self.leaf_childs = [self.root]
        que = deque([treeNode])
        while que:
            cur_node = que.popleft()

            left_child, right_child = cur_node.left, cur_node.right
            child_node_depth = cur_node.depth + 1

            if (left_child or right_child) and child_node_depth > self.leaf_childs[
                0
            ].depth:
                self.leaf_childs = []

            if left_child:
                left_child.parent = cur_node
                left_child.depth = child_node_depth
                que.append(left_child)
                self.leaf_childs.append(left_child)

            if right_child:
                right_child.parent = cur_node
                right_child.depth = child_node_depth
                que.append(right_child)
                self.leaf_childs.append(right_child)


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        custom_tree = CustomTree(root)
        childs = custom_tree.leaf_childs
        while not all(c == childs[0] for c in childs):
            for i in range(len(childs)):
                childs[i] = childs[i].parent
        return childs[0]
