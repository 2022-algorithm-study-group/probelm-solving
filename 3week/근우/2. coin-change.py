from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        NOT_VISIT = 2e9
        VISIT_BUT_NOT_FOUND = 2e9 + 1
        coins = list(filter(lambda x: x <= amount, coins))
        coins.sort(reverse=True)
        cache = [NOT_VISIT for _ in range(amount + 1)]

        def _dp(cur):
            if cache[cur] != NOT_VISIT:
                return cache[cur]
            elif cur == amount:
                return 0
            res = VISIT_BUT_NOT_FOUND
            for c in coins:
                next_cur = cur + c
                if next_cur <= amount:
                    res = min(res, 1 + _dp(next_cur))
            cache[cur] = res
            return res

        res = _dp(0)
        return res if res != VISIT_BUT_NOT_FOUND else -1
