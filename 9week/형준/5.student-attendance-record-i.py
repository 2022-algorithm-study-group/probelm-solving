## https://leetcode.com/problems/student-attendance-record-i/

class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') >= 2 or 'LLL' in s:
            return False      
        return True