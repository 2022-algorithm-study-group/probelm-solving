## https://leetcode.com/problems/longest-string-chain/
## 1 <= words.length <= 1000
## 1 <= words[i].length <= 16
from typing import List


class Solution:
    def longestStrChain(self, words):
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in xrange(len(w)))
        return max(dp.values())
