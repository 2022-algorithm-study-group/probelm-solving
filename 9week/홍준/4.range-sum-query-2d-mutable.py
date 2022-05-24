## https://leetcode.com/problems/range-sum-query-2d-mutable/

from typing import List

class NumMatrix:
    matrix = []
    R, C = 0, 0

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.R, self.C = len(matrix), len(matrix[0])

        self.partial_sum = [[] for _ in range(self.R)]
        for row in range(self.R):
            for col in range(self.C):
                if col == 0:
                    self.partial_sum[row].append(matrix[row][0])
                else:
                    self.partial_sum[row].append(self.partial_sum[row][-1] + matrix[row][col])

        # for row in range(self.R):
        #     print(self.partial_sum[row])

    def update(self, row: int, col: int, val: int) -> None:
        pre_val = self.matrix[row][col]
        self.matrix[row][col] = val
        diff = val - pre_val
        for c in range(col, self.C):
            self.partial_sum[row][c] += diff

        # for r in range(self.R):
        #     print(self.partial_sum[r])

        return

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        for r in range(row1, row2 + 1):
            if col1 == 0:
                result += self.partial_sum[r][col2]
            else:
                result += self.partial_sum[r][col2] - self.partial_sum[r][col1 - 1]

        # print(result)
        
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)

obj = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
obj.sumRegion(2,1,4,3)
obj.update(3,2,2)
obj.sumRegion(2,1,4,3)