class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        answer = 0
        n = len(costs) // 2
        sorted_costs = sorted(costs, key=lambda x: x[0]-x[1])
        for i in range(n):
            answer += sorted_costs[i][0]
        for i in range(n, 2*n):
            answer += sorted_costs[i][1]
        return answer
        