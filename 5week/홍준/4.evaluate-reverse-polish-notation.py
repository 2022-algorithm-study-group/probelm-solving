## https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = set(["+", "-", "*", "/"])
        
        def single_cal(num1, num2, operand):
            if operand == "+":
                return num2 + num1
            elif operand == "-":
                return num2 - num1
            elif operand == "*":
                return num2 * num1
            else:
                return int(num2 / num1)
        
        number_stack = []
        for element in tokens:
            if element not in operands:
                number_stack.append(int(element))
            else:
                num1 = number_stack.pop()
                num2 = number_stack.pop()
                number_stack.append(single_cal(num1, num2, element))
        return number_stack[-1]

print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))