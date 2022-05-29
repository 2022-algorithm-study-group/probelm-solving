## https://leetcode.com/problems/merge-k-sorted-lists/

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        val_list = []
        for head in lists:
            while head:
                val_list.append(head.val)
                head = head.next
        if not val_list:
            return None
        val_list.sort()
        # print(val_list)
        head = tail = ListNode(val_list[0], None)
        for val in val_list[1:]:
            tail.next = ListNode(val, None)
            tail = tail.next
        return head
        