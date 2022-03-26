from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return heights
        N, M = len(heights[0]), len(heights)
        res = []
        dp = [0 for i in range(N * M)]

        def dfs(i: int, j: int, w: int, h: int):
            ij = i * N + j
            if dp[ij] & w or heights[i][j] < h:
                return
            dp[ij] += w
            h = heights[i][j]
            if dp[ij] == 3:
                res.append([i, j])
            if i + 1 < M:
                dfs(i + 1, j, w, h)
            if i > 0:
                dfs(i - 1, j, w, h)
            if j + 1 < N:
                dfs(i, j + 1, w, h)
            if j > 0:
                dfs(i, j - 1, w, h)

        for i in range(M):
            dfs(i, 0, 1, heights[i][0])
            dfs(i, N - 1, 2, heights[i][N - 1])
        for j in range(N):
            dfs(0, j, 1, heights[0][j])
            dfs(M - 1, j, 2, heights[M - 1][j])
        return res
