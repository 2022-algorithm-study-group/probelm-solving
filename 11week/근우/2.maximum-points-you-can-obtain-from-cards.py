## https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_sum = sum_of_k = sum(cardPoints[len(cardPoints) - k:])
        for i in range(k):
            sum_of_k = sum_of_k + cardPoints[i] - cardPoints[-k+i]
            max_sum = max(sum_of_k,max_sum)
        return max_sum


print(Solution().maxScore(cardPoints=[100, 40, 17, 9, 73, 75], k=3))
