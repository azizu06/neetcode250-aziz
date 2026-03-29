class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows*cols-1
        while l<=r:
            m = (l+r)//2
            R, C = m//cols, m%cols
            if matrix[R][C] == target:
                return True
            elif matrix[R][C] < target:
                l = m+1
            else:
                r = m-1
        return False