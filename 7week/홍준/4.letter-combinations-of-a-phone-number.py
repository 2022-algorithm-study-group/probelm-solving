## https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List
from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        alphas = {"2" : ["a", "b", "c"], "3" : ["d", "e", "f"], "4" : ["g", "h", "i"], "5" : ["j", "k", "l"],
                    "6" : ["m", "n", "o"], "7" : ["p", "q", "r", "s"], "8" : ["t", "u", "v"], "9" : ["w", "x", "y", "z"]}

        if not digits:
            return []
        
        q = deque()
        q.extend([(alpha, 0) for alpha in alphas[digits[0]]])
        
        while len(q[0][0]) < len(digits):
            string, length = q.popleft()
            for alpha in alphas[digits[length+1]]:
                q.append((string + alpha, length + 1))
                
        return [string for string, length in q]

print(Solution().letterCombinations("23"))