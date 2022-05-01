from collections import deque


class Solution:
    def racecar(self, target: int) -> int:

        que = deque([(0, 0, 1)])
        while que:
            moves, pos, vel = que.popleft()
            if pos == target:
                return moves
            que.append((moves + 1, pos + vel, 2 * vel))
            if (pos + vel > target and vel > 0) or (pos + vel < target and vel < 0):
                que.append((moves + 1, pos, -vel / abs(vel)))
