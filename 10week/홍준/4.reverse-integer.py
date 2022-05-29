## https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            answer = -int(str(x)[1:][::-1])
        else:
            answer = int(str(x)[::-1])
        if -2**31 <= answer <= 2**31-1:
            return answer
        else:
            return 0