#https://leetcode.com/problems/subrectangle-queries/

class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self.data = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(col1, col2+1):
            for j in range(row1, row2+1):
               self. data[j][i] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.data[row][col]
