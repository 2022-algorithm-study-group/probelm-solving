class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        answer = 10**10
        for i in range(4):
            answer = min(answer, nums[-4+i]-nums[i])
        return answer
        