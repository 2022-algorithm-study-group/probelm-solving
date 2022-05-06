## https://leetcode.com/problems/median-of-two-sorted-arrays/

"""
Time Submitted
Status
Runtime
Memory
Language
05/03/2022 18:29	Accepted	82 ms	14.2 MB	python3 -> 99.30 / 69.44
05/03/2022 18:28	Accepted	126 ms	14.2 MB	python3
05/03/2022 18:28	Accepted	139 ms	14.1 MB	python3
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        
        merged.sort()
        
        length = len(merged)
        if length%2 == 0:
            return (merged[length//2] + merged[length//2 - 1])/2
        else:
            return merged[length//2]