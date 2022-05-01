## https://leetcode.com/problems/median-of-two-sorted-arrays/

import math
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total_length = len(A) + len(B)
        total_mid = total_length // 2
        if len(B) < len(A):
            A, B = B, A
        
        left, right = 0, len(A) - 1
        while True:
            A_top = (left + right) // 2
            B_top = total_mid - A_top - 2

            left_A_max = A[A_top] if A_top >= 0 else -math.inf
            right_A_min = A[A_top + 1] if A_top + 1 < len(A) else math.inf
            left_B_max = B[B_top] if B_top >= 0 else -math.inf
            right_B_min = B[B_top + 1] if B_top + 1 < len(B) else math.inf

            if left_A_max <= right_B_min and left_B_max <= right_A_min:
                if total_length % 2:
                    return min(right_A_min, right_B_min)
                return (max(left_A_max, left_B_max) + min(right_A_min, right_B_min)) / 2
            elif left_A_max > right_B_min:
                right = A_top - 1
            else:
                left = A_top + 1

print(Solution().findMedianSortedArrays([1,2], [3,4]))