## https://leetcode.com/problems/maximum-split-of-positive-even-integers/
# 1 <= finalSum <= 10**10

from bisect import bisect_left
from collections import defaultdict
from email.policy import default
from typing import List

# Sk = K*(K+1)/2 Sk <= 10**10
# Sk = K*(K+1) = 28
# K = 5
# K <=10**5
# 전부다 포함시킨 뒤 빼기
# finalsum = 28
# 14
# idx = 5
# total_sum = arr[k] = [1,2,3...5] = 15
# total_sum - final_sum = k
#
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum%2!=0:
            return []
        finalSum/=2
        arr = [int(k*(k+1))/2 for k in range(10**5+1)]
        idx = bisect_left(arr,finalSum)
        total_sum = arr[idx]
        k = total_sum - finalSum
        return list(filter(lambda a: a!=2*k,[2*i for i in range(1,idx+1)]))


print(Solution().maximumEvenSplit(9999999998))
print(Solution().maximumEvenSplit(28))
print(Solution().maximumEvenSplit(12))
print(Solution().maximumEvenSplit(7))