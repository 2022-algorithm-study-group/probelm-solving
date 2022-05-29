## https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        LIMIT = 2**31
        res = 0
        res_number_of_digits = 0
        x_number_of_digits = 11
        is_postive = x > 0
        if not is_postive:
            x *= -1
        for i in range(x_number_of_digits, -1, -1):
            cur = (x//(10**i)) % 10
            if res + cur*(10**(res_number_of_digits)) >= LIMIT:
                return 0

            res += cur*(10**(res_number_of_digits))
            if res != 0:
                res_number_of_digits += 1
        return res if is_postive else -res
Solution().reverse(123)