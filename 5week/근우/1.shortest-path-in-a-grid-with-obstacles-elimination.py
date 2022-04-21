## https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 40
# 1 <= k <= m * n
# grid[i][j] is either 0 or 1.
# grid[0][0] == grid[m - 1][n - 1] == 0
from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], K: int) -> int:
        R = len(grid)
        C = len(grid[0])
        DIR = [[0,1],[0,-1],[1,0],[-1,0]]
        is_visit = [[[False for _ in range(K+1)] for _ in range(C)] for _ in range(R)] ## is_visit[m][n][k]
        is_visit[0][0][0] = True
        que =deque([(0,0,0,0)]) # r, c, k, depth
        while que:
            r, c, k, depth = que.popleft()
            if r == R-1 and c == C-1:
                return depth
            for dr,dc in DIR:
                nr, nc = r+dr,c+dc
                if 0<=nr<R and 0<=nc<C:
                    nk = k+1 if grid[nr][nc] == 1 else k
                    if nk <= K and not is_visit[nr][nc][nk]:
                        is_visit[nr][nc][nk] = True
                        que.append((nr,nc,nk,depth+1))
        return -1