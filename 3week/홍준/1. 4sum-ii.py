from typing import List
from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dict1, dict2 = defaultdict(int), defaultdict(int)
        answer = 0
        
        for n1 in nums1:
            for n2 in nums2:
                dict1[n1+n2] += 1
        
        for n3 in nums3:
            for n4 in nums4:
                dict2[n3+n4] += 1
        
        for key in dict1.keys():
            answer += dict1[key] * dict2[-key]
        
        return answer