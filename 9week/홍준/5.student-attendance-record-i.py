## https://leetcode.com/problems/student-attendance-record-i/

class Solution:
    def checkRecord(self, s: str) -> bool:
        cnt = 0
        abs_cnt = 0
        for status in s:
            if status == "L":
                cnt += 1
                if cnt == 3:
                    return False
            elif status == "A":
                abs_cnt += 1
                if abs_cnt == 2:
                    return False
                cnt = 0
            else:
                cnt = 0
        return True