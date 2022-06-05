## https://leetcode.com/problems/longest-string-chain/

from typing import List
from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = defaultdict(int)
        words.sort(key=lambda x:len(x))
        for word in words:
            dp[word] = 1
        for word in words:
            if len(word) == 1:
                continue
            for i in range(len(word)):
                removed = word[:i] + word[i+1:]
                dp[word] = max(dp[word], dp[removed] + 1)
        return max([val for val in dp.values()])

print(Solution().longestStrChain(["a","b","ba","bca","bda","bdca"]))