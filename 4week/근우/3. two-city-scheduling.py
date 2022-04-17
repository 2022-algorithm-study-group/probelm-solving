from functools import reduce
from typing import List

# 2 <= costs.length <= 100
# 작은것들 큰것들 나누기 왼쪽 오른쪽 나누기
# 왼쪽 5개 오른쪽 1개
# 5개 5개씩 뽑아야함
# 왼쪽 4개 뽑고 오른쪽6개중에 하나는 왼쪽껄 뽑아야함
# 많이 나온쪽에서 큰것을 필수적으로 선택 해야하는 갯수만큼 큰것과 작은것의 차이가 작은것을 뽑는다.


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs) >> 1
        left_things = []
        right_things = []
        for i, cost in enumerate(costs):
            if cost[0] < cost[1]:
                left_things.append(cost)
            else:
                right_things.append(cost)
        more_things = (
            left_things if len(left_things) > len(right_things) else right_things
        )
        small_things = (
            right_things if len(left_things) > len(right_things) else left_things
        )
        diff_list = [(abs(cost[1] - cost[0]), i) for i, cost in enumerate(more_things)]
        diff_list.sort()
        for i in range(len(more_things) - N):
            idx = diff_list[i][1]
            more_things[idx] = (max(more_things[idx]), max(more_things[idx]))
        return reduce(lambda a, b: a + min(b), small_things + more_things, 0)
