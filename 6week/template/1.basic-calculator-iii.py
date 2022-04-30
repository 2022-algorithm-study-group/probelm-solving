## https://leetcode.com/problems/basic-calculator-iii/

class Solution:
    def calculate(self, s: str) -> int:
        operands = set(["+", "-", "*", "/", "(", ")"])
        order = {"+" : 0, "-" : 0, "*" : 1, "/" : 1, "(" : -1, ")" : -1}
        postfix = []
        operand_stack = []

        ## make postfix list
        num = ""
        for idx, element in enumerate(s):         
            if element.isdigit():
                num = num + element
                if idx == len(s)-1 or s[idx+1] in operands:
                    postfix.append(int(num))
                    num = ""
            elif element == "(":
                operand_stack.append(element)
            elif element == ")":
                while operand_stack:
                    operand = operand_stack.pop()
                    if operand == "(":
                        break
                    else:
                        postfix.append(operand)
            else:
                if not operand_stack:
                    operand_stack.append(element)
                else:
                    while operand_stack and order[operand_stack[-1]] >= order[element]:
                        postfix.append(operand_stack.pop())
                    if element != "(":
                        operand_stack.append(element)
        while operand_stack:
            postfix.append(operand_stack.pop())

        ## calculate postfix list
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
        for element in postfix:
            if type(element) is int:
                number_stack.append(element)
            else:
                num1 = number_stack.pop()
                num2 = number_stack.pop()
                number_stack.append(single_cal(num1, num2, element))
        return number_stack[-1]

print(Solution().calculate("2*(5+5*2)/3+(6/2+8)"))