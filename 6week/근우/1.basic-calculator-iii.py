## https://leetcode.com/problems/basic-calculator-iii/
class Solution:
    def calculate(self, s: str) -> int:
        # 후위 표현식 만들기
        # 후위 표현식 계산하기
        # 2*2+3 => 22*3+ => 4+3=7
        # 2+2*3 => 223*+ =>
        # 2*(2+3) => 223+* => (2+3)*2
        return 1
    def make_postfix_notation(self, s):
        OP = {'+', '-', '/', '*', '(', ')'}
        res = []
        cur_num = ''
        for w in s:
            if w in OP:
                res.append(int(cur_num))
                res.append(w)
                cur_num = ''
            else:
                cur_num+=w
        if cur_num != '':
            res.append(int(cur_num))
        return res
print(Solution().make_postfix_notation('23*2+3'))