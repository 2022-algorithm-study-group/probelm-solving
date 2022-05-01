## https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        size = 1
        tmp = head
        while tmp.next:
            size += 1
            tmp = tmp.next
        if size == n:
            return head.next
        
        cnt = 0
        tmp = head
        while True:
            if cnt == size - n - 1:
                tmp.next = tmp.next.next
                break
            cnt += 1
            tmp = tmp.next
            
        return head