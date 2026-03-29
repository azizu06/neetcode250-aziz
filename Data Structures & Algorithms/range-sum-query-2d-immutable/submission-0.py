class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.grid = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        for i in range(len(matrix)):
            prefix = 0
            r = i+1
            for j in range(len(matrix[i])):
                c = j+1
                prefix += matrix[i][j]
                top = self.grid[r-1][c]
                self.grid[r][c] = prefix + top

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        bottomRight = self.grid[row2][col2]
        left = self.grid[row2][col1-1]
        top = self.grid[row1-1][col2]
        topLeft = self.grid[row1-1][col1-1]
        return bottomRight - left - top + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)