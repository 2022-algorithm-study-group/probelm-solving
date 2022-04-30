## https://leetcode.com/problems/single-threaded-cpu/

import heapq
from typing import List
from collections import deque

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        PROCESSING_TIME, START_TIME, IDX = 0, 1, 2
        order = []
        time_heap = []
        sorted_tasks = deque(sorted([(processing_time, start_time, idx) for idx, [start_time, processing_time] in enumerate(tasks)], key=lambda x:x[1]))

        def heap_process(time_heap, now):
            candidates = [heapq.heappop(time_heap)]
            smallest_processing_time = candidates[0][PROCESSING_TIME]
            while time_heap and time_heap[0][PROCESSING_TIME] == smallest_processing_time:
                candidates.append(heapq.heappop(time_heap))
            candidates.sort(key=lambda x:-x[IDX])
            task = candidates.pop()
            order.append(task[IDX])
            for candidate in candidates:
                heapq.heappush(time_heap, candidate)
            return now + task[PROCESSING_TIME]


        now = sorted_tasks[0][START_TIME]
        while sorted_tasks:
            while sorted_tasks and sorted_tasks[0][START_TIME] <= now:
                heapq.heappush(time_heap, sorted_tasks.popleft())
            if not time_heap:
                now = sorted_tasks[0][START_TIME]
                while sorted_tasks and sorted_tasks[0][START_TIME] <= now:
                    heapq.heappush(time_heap, sorted_tasks.popleft())
            # print(time_heap)
            now = heap_process(time_heap, now)
        
        while time_heap:
            now = heap_process(time_heap, now)
        
        return order
        
        
print(Solution().getOrder([[5,6],[9,4],[3,9],[3,7],[1,1],[6,9],[9,1]]))