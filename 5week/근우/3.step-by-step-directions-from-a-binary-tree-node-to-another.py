# Definition for a binary tree node.
from collections import deque
from inspect import trace


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        startNode,destNode = None,None
        root.parent = None
        def dfs(root):
            nonlocal startNode,destNode
            if not root:
                return
            
            if root.val == startValue:
                startNode = root
            if root.val ==destValue:
                destNode = root
            
            if root.left:
                root.left.parent = root
                dfs(root.left)
            if root.right:
                root.right.parent = root
                dfs(root.right)
        dfs(root)
        is_visit = [False for _ in range(10**5+1)]
        que = deque([(startNode,'')]) # curNode, tracing_routes
        while que:
            node, traces = que.popleft()
            if node == destNode:
                return traces
            for next_node, dir in [(node.parent,'U'), (node.left,'L'), (node.right,'R')]:
                if next_node and not is_visit[next_node.val]:
                    is_visit[next_node.val] = True
                    que.append((next_node,traces+dir))
