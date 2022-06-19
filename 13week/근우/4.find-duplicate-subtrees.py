## https://leetcode.com/problems/find-duplicate-subtrees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# leaf node에서부터 올라가면서 check 어떻게 => 현재 depth에서 겹치는놈이 있는지 체크
# parent = set{}

from collections import defaultdict


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        parentMap = {}
        LEFT, RIGHT = 0, 1
        st = [root]
        leaf_nodes = []
        while st:
            node = st.pop()
            l, r = node.left, node.right
            for c in [l,r]:
                if c:
                    parentMap[c] = node
                    st.append(c)
            if not l and not r:
                leaf_nodes.append(node)
        def _solve(nodes):
            ## 노드들을 읽으면서 값이 같고 parent가 같고 구조가 같은녀석들을 묶어서 _solve() parent들을 보내버림
            node_info = defaultdict(defaultdict(list)) ## [parent_value][left_or_right] = []
            for node in nodes:
                p = parentMap[node]
                if p.left == node:
                    node_info[p.value][LEFT].append(node)
                elif p.right == node:
                    node_info[p.value][RIGHT].append(node)
            

