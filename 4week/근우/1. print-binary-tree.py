# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def _findDepth(node):
            if not node:
                return 0
            return 1 + max(_findDepth(node.left), _findDepth(node.right))

        R = _findDepth(root)
        C = 2 ** (R) - 1
        res = [["" for _ in range(C)] for _ in range(R)]
        res[0][C >> 1] = str(root.val)
        que = deque([(root, 0, C >> 1)])  # cur_node, row, col
        while que:
            cur_depth_node = []
            while que:
                cur_depth_node.append(que.popleft())
            for node, r, c in cur_depth_node:
                if node.left:
                    que.append((node.left, r + 1, c - 2 ** (R - r - 2)))
                    res[r + 1][c - 2 ** (R - r - 2)] = str(node.left.val)
                if node.right:
                    que.append((node.right, r + 1, c + 2 ** (R - r - 2)))
                    res[r + 1][c + 2 ** (R - r - 2)] = str(node.right.val)
        return res
