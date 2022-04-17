from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        TOTAL_ALPHABET_COUNT = 26
        FIRST_ASCII, LAST_ASCII = ord("a"), ord("z")
        total_shifts = []
        cur_shift = sum(shifts)
        for i in range(len(shifts)):
            if i != 0:
                cur_shift -= shifts[i - 1]
            total_shifts.append(cur_shift % TOTAL_ALPHABET_COUNT)
        print(total_shifts)
        res = str()
        for idx, shift in enumerate(total_shifts):
            cur_ascii = ord(s[idx]) + shift
            if cur_ascii > LAST_ASCII:
                cur_ascii = cur_ascii - LAST_ASCII + FIRST_ASCII - 1
            res += chr(cur_ascii)
        return res


Solution().shiftingLetters("ruu", [26, 9, 17])


26
