## https://leetcode.com/problems/score-after-flipping-matrix/

from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        answer = 2 ** (n - 1) * m
        for j in range(1, n):
            cnt = 0
            for i in range(m):
                if grid[i][j] == grid[i][0]:
                    cnt += 1
            answer += max(cnt, m - cnt) * 2 ** (n - 1 - j)
        return answer

print(Solution().matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))