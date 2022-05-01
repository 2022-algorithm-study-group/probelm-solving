## https://leetcode.com/problems/race-car/

# 2^(k-1) - 1 <= target <= 2^k - 1
# target = 2^(k-1)-1 + X
# 0<=X<=2^(k-1)
# check
# 1023 -> 1023 -> 1023 ->1024
#        speed = -1 speed = 1
# 3 5 7
# 3 3 3 4 5
# 3 7 7 6 5
from bisect import bisect_left


class Solution:
    def racecar(self, target: int) -> int:
        arr = [2**i - 1 for i in range(15)]
        idx = bisect_left(arr,target)
        left_diff = target - arr[idx-1]
        right_diff = arr[idx] - target
        if left_diff<=right_diff:
            idx-=1
        cnt =idx
        while target!=arr[idx]:
            left_diff = target - arr[idx-1]
            right_diff = arr[idx] - target
            target = min(left_diff, right_diff)
            idx = bisect_left(arr, target)
            if left_diff==right_diff:
                cnt+= idx
            else:
                cnt+=(idx+1)

        return cnt


print(Solution().racecar(2)) #==4)
print(Solution().racecar(5))##==7)
