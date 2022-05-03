## https://leetcode.com/problems/regular-expression-matching/

"""
Time Submitted
Status
Runtime
Memory
Language
05/03/2022 18:39	Accepted	94 ms	14 MB	python3
05/03/2022 18:38	Accepted	104 ms	14 MB	python3
05/03/2022 18:38	Accepted	104 ms	14 MB	python3
05/03/2022 18:37	Accepted	80 ms	14 MB	python3
05/03/2022 18:36	Accepted	97 ms	13.9 MB	python3
05/03/2022 18:36	Accepted	64 ms	13.9 MB	python3  -> 62.60%
05/03/2022 18:36	Accepted	92 ms	14 MB	python3
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return True if re.fullmatch(p, s) else False