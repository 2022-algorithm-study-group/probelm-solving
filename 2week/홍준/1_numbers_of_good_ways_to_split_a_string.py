from collections import defaultdict

def good(left, right):
    cnt_left, cnt_right = 0, 0
    for key in left.keys():
        if left[key] > 0:
            cnt_left += 1
    for key in right.keys():
        if right[key] > 0:
            cnt_right += 1
    if cnt_left == cnt_right:
        return True
    return False

class Solution:

    def numSplits(self, s: str) -> int:
        cnt = 0
        left = defaultdict(int)
        right = defaultdict(int)
        
        for i in range(0, len(s)):
            if i == 0:
                left[s[i]] += 1
            else:
                right[s[i]] += 1
    
        if good(left, right):
            cnt += 1
        
        for i in range(1, len(s)-1):
            left[s[i]] += 1
            right[s[i]] -= 1
            if good(left, right):
                cnt += 1
        return cnt