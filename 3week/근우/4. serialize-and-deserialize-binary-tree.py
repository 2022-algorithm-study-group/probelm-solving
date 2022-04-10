from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    def serialize(self, root):
        str_list = []
        que = deque([root])
        while que:
            p = que.popleft()
            if p == None:
                str_list.append("N")
                continue
            str_list.append(str(p.val))
            que.append(p.left)
            que.append(p.right)
        return " ".join(str_list)

    def deserialize(self, data):
        str_list = data.split()
        if not str_list:
            return []
        ans = []
        que = deque([str_list[0]])
        while que:
            p = que.popleft()
            if p == None:
                ans.append(None)
                continue
            cur_node = TreeNode(p)
            ans.append(cur_node)
            que.append(p.left)
            que.append(p.right)
        return ans
