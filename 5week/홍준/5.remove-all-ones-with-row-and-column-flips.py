## https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/

from typing import List

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        base = grid[0]
        opposite = [1-i for i in base]
        for row in grid:
            if row != base and row != opposite:
                return False
        return True