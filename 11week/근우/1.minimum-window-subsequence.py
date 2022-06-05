## https://leetcode.com/problems/minimum-window-subsequence/

## fist approach is binary search + DP
## Logic
## 1. save character's position in the array
## 2. and search the array
## 3. and cache the search information =>
### cache[s2_index_num][s1_index_num] => so only need to search once.
## timeComplexity is N
## for example
## s1 = acabacb s2 = ab
## C[a] = [0,2,4], C[b] = [3,6], C[c] = [1,5]
## then search

from bisect import bisect_right
from collections import defaultdict, deque


class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        character_dict = defaultdict(list)
        out_put = ""
        min_len = NO_MATCHING = 2e9
        answer_idx = None
        cache = [[None for _ in range(len(s1))] for _ in range(100)]
        for i, c in enumerate(s1):
            character_dict[c].append(i)

        for s1_idx in character_dict[s2[0]]:
            def search(s1_idx, s2_idx):
                if s2_idx == len(s2):
                    return 0

                if cache[s2_idx][s1_idx]:
                    return cache[s2_idx][s1_idx]

                s2_idx_char_info = character_dict[s2[s2_idx]]
                idx = bisect_right(s2_idx_char_info, s1_idx)
                if idx == len(s2_idx_char_info):
                    cache[s2_idx][s1_idx] = NO_MATCHING
                    return NO_MATCHING
                next_s1_idx = s2_idx_char_info[idx]

                cache[s2_idx][s1_idx] = (next_s1_idx - s1_idx) + search(
                    next_s1_idx, s2_idx+1)
                return cache[s2_idx][s1_idx]
            cur_len = search(s1_idx, 1)
            if cur_len < min_len:
                answer_idx = s1_idx
                min_len = cur_len

        if min_len == NO_MATCHING:
            return ""

        s1_idx = answer_idx
        s2_idx = 0
        output = ""
        while s2_idx!=len(s2):
            c = s1[s1_idx]
            if s2[s2_idx] == c:
                s2_idx+=1
            output += c
            s1_idx+=1
        return output



# print(Solution().minWindow("abcdebdde","bde"))
# print(Solution().minWindow("jmeqksfrsdcmsiwvaovztaqenprpvnbstl", "u"))
# print(Solution().minWindow("jmeqksfrsdcmsiwvaovztaqenprpvnbstl", "fwz"))


## second approach is using stack
## using count_dict

class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        deq = deque([])
        s2_idx = 0
        output = ""
        s1_0_idx_count 
        for c in s1:

            if c == s2[s2_idx]:
                s2_idx+=1
            else:
                while s2_idx < len(s2) and c == s2[0] and s2[s2_idx] != c and len(deq) > 0:
                    deq.popleft()

            if s2_idx >= 1:
                deq.append(c)

            if s2_idx == len(s2):
                if output == "" or len(output) > len(deq):
                    output = "".join(deq)
                s2_idx = 0
                deq = deque([])

        return output


print(Solution().minWindow("ggj", "ggj"))
# print(Solution().minWindow("abcdebdde", "bde"))
# print(Solution().minWindow("jmeqksfrsdcmsiwvaovztaqenprpvnbstl", "u"))
# print(Solution().minWindow("jmeqksfrsdcmsiwvaovztaqenprpvnbstl", "fwz"))
print(Solution().minWindow("cnhczmccqouqadqtmjjzl", "cm"))
