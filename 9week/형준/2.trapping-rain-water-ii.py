## https://leetcode.com/problems/trapping-rain-water-ii/

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        self.board = heightMap
        self.visit = set()
        answer = 0
        for i in range(1, len(self.board)-1):
            for j in range(1, len(self.board[i])-1):
                if (i, j) in self.visit:
                    continue
                cnt, visit = self.bfs(i, j)
                print(i, j, cnt)
                answer += cnt
                self.visit.update(visit)
                
        return answer
                
    def bfs(self, i, j):
        queue = deque([(i, j)])
        visit = set()
        cnt = 1
        len_x, len_y = len(self.board), len(self.board[0])
        while queue:
            x, y = queue.popleft()
            
            if not (1 <= x < len_x-1 and 1 <= y < len_y-1):
                return 0, set()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if not (0 <= nx < len_x and 0 <= ny < len_y):
                    continue
                    
                if self.board[x][y] >= self.board[nx][ny]:
                    visit.add((nx, ny))
                    queue.append((nx, ny))
                    cnt += 1
                    
        return cnt, visit