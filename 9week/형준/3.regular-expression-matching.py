## https://leetcode.com/problems/regular-expression-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #return True if re.fullmatch(p, s) else False
        
        s, p = ' ' + s, ' ' + p
        len_s, len_p = len(s), len(p)
        dp = [[False]*len_p for _ in range(len_s)]
        dp[0][0] = True
        
        for i in range(1, len_p):
            if p[i] == '*':
                dp[0][i] = dp[0][i-2]
                    
        for i in range(1, len_s):
            for j in range(1, len_p):
                if p[j] == s[i] or p[j] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == '*':
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and p[j-1] in {s[i], '.'})
                    
        return dp[-1][-1]