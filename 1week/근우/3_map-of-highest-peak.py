from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        NOT_VISIT = -1
        M, N = len(isWater), len(isWater[0])
        map = [[NOT_VISIT for i in range(N)] for j in range(M)]
        que = deque([])
        for i in range(M):
            for j in range(N):
                if isWater[i][j] == 1:
                    map[i][j] = 0
                    que.append([i, j])

        dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]
        while que:
            cur_pos = que.popleft()
            for i in range(4):
                next_y, next_x = cur_pos[0] + dy[i], cur_pos[1] + dx[i]
                if (
                    0 <= next_y < M
                    and 0 <= next_x < N
                    and map[next_y][next_x] == NOT_VISIT
                ):
                    map[next_y][next_x] = map[cur_pos[0]][cur_pos[1]] + 1
                    que.append([next_y, next_x])
        return map
