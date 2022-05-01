## https://leetcode.com/problems/single-threaded-cpu/
## aproach
## 1. read all task that able in current time
## 2. process shortest_processing_time
from typing import List
import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        que = []
        for i,t in enumerate(tasks):
            t.append(i)
        tasks.sort()
        c_t = 0
        for e_t,p_t,i in tasks:
            while c_t < e_t:
                if que:
                    c_p_t, num = heapq.heappop(que)
                    c_t +=c_p_t
                    res.append(num)
                else:
                    c_t = e_t
                    heapq.heappush(que,(p_t,i))
                    break
            else:
                heapq.heappush(que,(p_t,i))
        while que:
            _, num = heapq.heappop(que)
            res.append(num)
        return res


print(Solution().getOrder([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]))
print(Solution().getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]))

