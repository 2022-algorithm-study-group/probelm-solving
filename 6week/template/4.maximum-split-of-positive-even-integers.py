## https://leetcode.com/problems/maximum-split-of-positive-even-integers/

from typing import List

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
        i, sum = 0, 0
        answer = []
        while sum + i < finalSum:
            i += 2
            sum += i
            answer.append(i)
        if sum == finalSum:
            return answer
        last = answer.pop()
        answer.append(finalSum-sum+last)
        return answer

print(Solution().maximumEvenSplit(28))
