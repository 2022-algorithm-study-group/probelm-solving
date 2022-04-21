## https://leetcode.com/problems/find-leaves-of-binar# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ref = defaultdict(list)
        def dfs(node):
            if not node:
                return 0
            if node:
                cur = 1+max(dfs(node.left),dfs(node.right))
            ref[cur].append(node.val)
            return cur
        dfs(root)
        return [v for v in ref.values()]