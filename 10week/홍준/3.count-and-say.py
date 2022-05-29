## https://leetcode.com/problems/count-and-say/

class Solution:
    def say(self, digits):
        digit_list = [int(a) for a in digits]
        new_digits = []
        num, cnt = digit_list[0], 1
        for i in range(1, len(digit_list)):
            if digit_list[i] == num:
                cnt += 1
                continue
            else:
                new_digits.extend([cnt, num])
                num, cnt = digit_list[i], 1
        new_digits.extend([cnt, num])
        return "".join(map(str, new_digits))
            
    
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.say(self.countAndSay(n-1))