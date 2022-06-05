## https://leetcode.com/problems/minimum-window-subsequence/

# dp[j][e] = s
# s1[s:e+1]이 s2[:j]를 포함한다는 것을 만족하는 최대 인덱스 값 s
# 만약에 s1[e+1] = s2[j] 라면, dp[j+1][e+1] = dp[j][e]
# 만약 다르다면, dp[j+1][e+1] = dp[j+1][e]
# dp[j+1][e+1] = dp[j+1][e], dp[j][e+1]

class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        base_len, target_len = len(s1), len(s2)
        dp = [[0] * base_len for _ in range(target_len)]
        for i in range(base_len):
            dp[0][i] = i
        for j in range(target_len-1):
            for e in range(base_len-1):
                if s1[e+1] == s2[j]:
                    dp[j+1][e+1] = dp[j][e]
                else:
                    dp[j+1][e+1] = dp[j+1][e]
        for row in range(target_len):
            for col in range(base_len):
                print(s1[dp[row][col]:col], end=" ")
            print()

Solution().minWindow("abcdebdde", "bde")

