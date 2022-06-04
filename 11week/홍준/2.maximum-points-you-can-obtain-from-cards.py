## https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints)
        answer = sum(cardPoints[size-k:size])
        partial_sum = answer
        for i in range(k):
            partial_sum += cardPoints[(size + i) % size] - cardPoints[(size - k + i) % size]
            answer = max(answer, partial_sum)
        return answer