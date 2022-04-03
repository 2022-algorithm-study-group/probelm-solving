from typing import List
import sys

sys.setrecursionlimit(10 ** 5)
# m*n matrix
# m == points.length
# n == points[r].length
# 1 <= m, n <= 10**5
# 1 <= m * n <= 10**5
# 0 <= points[r][c] <= 10**5
# using dp
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = [0] * n
        for i in range(m):
            new_dp = dp[:]
            for j in range(1, n):
                new_dp[j] = max(new_dp[j - 1] - 1, new_dp[j])
            for j in range(n - 2, -1, -1):
                new_dp[j] = max(new_dp[j + 1] - 1, new_dp[j])
            dp = [points[i][j] + new_dp[j] for j in range(n)]
        return max(dp)


class Solution2:
    def maxPoints(self, points: List[List[int]]) -> int:
        R, C = len(points), len(points[0])
        cache = [[0 for _ in range(C)] for _ in range(R)]
        answer = 0
        for r in range(R):
            for c in range(C):
                if r == 0:
                    cache[r][c] = points[r][c]
                else:
                    for bc in range(C):
                        cache[r][c] = max(
                            cache[r][c], points[r][c] + cache[r - 1][bc] - abs(c - bc)
                        )
        for c in range(C):
            answer = max(answer, cache[R - 1][c])
        return answer


print(Solution().maxPoints([[1, 2, 3], [1, 5, 1], [3, 1, 1]]))
