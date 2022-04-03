from typing import List

LIMIT = 24 * 60
MAX = LIMIT


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = list(map(lambda x: int(x[:2]) * 60 + int(x[3:]), timePoints))
        timePoints.sort()
        timePoints.append(timePoints[0] + LIMIT)
        ans = MAX
        for i in range(len(timePoints) - 1):
            ans = min(ans, timePoints[i + 1] - timePoints[i])
        return ans


print(Solution().findMinDifference(timePoints=["23:59", "00:00"]))
