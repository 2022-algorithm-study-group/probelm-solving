from itertools import combinations

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timeSet = set(timePoints)
        if len(timeSet) != len(timePoints):
            return 0
        answer = 60 * 24
        for t1, t2 in combinations(timeSet, 2):
            time1 = 60 * int(t1[:2]) + int(t1[3:])
            time2 = 60 * int(t2[:2]) + int(t2[3:])
            diff = min(1440 - abs(time1 - time2), abs(time1 - time2))
            if diff < answer:
                answer = diff
        return answer