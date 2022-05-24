## https://leetcode.com/problems/reconstruct-itinerary/

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs():
            if len(answer) == end_path_len:
                self.end_flag = True
                return
            
            cur = answer[-1]
            for next in sorted(graph[cur]):
                if graph[cur][next] <= 0:
                    continue
                graph[cur][next] -= 1
                answer.append(next)
                dfs()
                if self.end_flag:
                    return
                answer.pop()
                graph[cur][next] += 1
                
        
        graph = defaultdict(lambda : defaultdict(int))
        for a, b in tickets:
            graph[a][b] += 1
            
        self.end_flag = False
        end_path_len = len(tickets) + 1
        answer = ['JFK']
        dfs()
        return answer
        