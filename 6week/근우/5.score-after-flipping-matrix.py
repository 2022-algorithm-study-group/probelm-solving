## https://leetcode.com/problems/score-after-flipping-matrix/
class Solution:
    def matrixScore(self, A):
        M, N = len(A), len(A[0])
        res = (1 << N - 1) * M
        for j in range(1, N):
            cur = sum(A[i][j] == A[i][0] for i in range(M))
            res += max(cur, M - cur) * (1 << N - 1 - j)
        return res

Solution().matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]])