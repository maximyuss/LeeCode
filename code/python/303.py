# https://leetcode.com/problems/range-sum-query-2d-immutable/
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self._prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self._prefix[i][j] = matrix[i - 1][j - 1] + self._prefix[i - 1][j] + self._prefix[i][j - 1] - self._prefix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self._prefix[row2 + 1][col2 + 1] 
            - self._prefix[row1][col2 + 1] 
            - self._prefix[row2 + 1][col1] 
            + self._prefix[row1][col1])
