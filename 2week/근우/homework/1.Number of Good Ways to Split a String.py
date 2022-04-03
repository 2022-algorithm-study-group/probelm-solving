# 1 <= s.length <= 10**5
from itertools import count


class Solution:
    def numSplits(self, s: str) -> int:
        count_by_char = {}
        for c in s:
            count_by_char[c] = count_by_char[c] + 1 if c in count_by_char else 1
        set = {}
        res = 0
        for c in s:
            set.add(c)
            count_by_char[c] -= 1
            if count_by_char[c] == 0:
                count_by_char.pop(c)
            if len(set) == len(count_by_char):
                res += 1
        return res
