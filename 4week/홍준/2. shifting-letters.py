def shift_result(alphabet, shift_num):
    idx = (ord(alphabet) - 97 + shift_num) % 26 + 97
    return chr(idx)

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        answer = ""
        total = sum(shifts)
        total_shifts = []
        for shift in shifts:
            total_shifts.append(total)
            total -= shift
        # print(total_shifts)
        for idx, alphabet in enumerate(s):
            answer += shift_result(alphabet, total_shifts[idx])
        return answer