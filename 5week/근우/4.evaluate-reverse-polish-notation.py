# ## https://leetcode.com/problems/evaluate-reverse-polish-notation/
# from typing import List


from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        operator = set({"+", "*", "/", "-"})
        for token in tokens:
            if token in operator:
                num1, num2 = nums.pop(), nums.pop()
                if token == "+":
                    nums.append(num2 + num1)
                elif token == "*":
                    nums.append(int(num2 * num1))
                elif token == "-":
                    nums.append(num2 - num1)
                else:
                    nums.append(int(num2 / num1))
            else:
                nums.append(int(token))
        return nums[0]
