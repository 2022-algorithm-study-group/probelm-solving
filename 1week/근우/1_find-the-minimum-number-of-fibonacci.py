from bisect import bisect_left


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        _list = [1, 1]
        while _list[-1] + _list[-2] <= k:
            _list.append(_list[-1] + _list[-2])
        res, cnt = k, 0
        while res != 0:
            cur = bisect_left(_list, res)
            if cur == len(_list) or _list[cur] > res:
                cur -= 1
            res -= _list[cur]
            cnt += 1
        return cnt
