from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0
        nums.sort()
        ans = 2e9
        for l in range(0, 4, 1):
            r = 3 - l
            ans = min(ans, nums[-1 - r] - nums[l])
        return ans


print(Solution().minDifference([1, 5, 0, 10, 14]))
