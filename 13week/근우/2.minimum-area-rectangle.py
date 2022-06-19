## https://leetcode.com/problems/minimum-area-rectangle/

# 한점을 기준으로 x좌표 같은놈들, y좌표가 같은놈들을 찾는다.

# 현재 점 p1
# x좌표 같은점들 모음 Set(Xp)
# y좌표 같은점들 모음 Set(Yp)

# 다시 탐색하면서 Xp와 y좌표가 있고 Yp와 x좌표가 있으면 넓이 계산을 한다.

# Timecomplexity
# *(500l+500) 2N^2


from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = NO_AREA = 2e9
        for i, p in enumerate(points):
            if p[0] == 3 and p[1] ==1:
                print()
            Xp = set()
            Yp = set()
            for j in range(i+1, len(points)):
                p2 = points[j]
                if p[0] == p2[0]:
                    Yp.add(p2[1])
                elif p[1] == p2[1]:
                    Xp.add(p2[0])
            for j in range(i+1, len(points)):
                p2 = points[j]
                if p2[0] in Xp and p2[1] in Yp:
                    min_area = min(min_area, abs((p[0] -p2[0])*(p[1]-p2[1])))
        if min_area == NO_AREA:
            return 0
        return min_area

Solution().minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]])