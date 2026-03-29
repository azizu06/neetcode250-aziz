class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        r1, c1, r2, c2 = 0, 0, rows-1, cols-1
        l, r = r1*cols+c1, r2*cols+c2
        while l<=r:
            mid = (l+r)//2
            m1, m2 = mid//cols, mid%cols 
            if matrix[m1][m2] == target:
                return True
            elif matrix[m1][m2] > target:
                r = mid-1
            else:
                l = mid+1
        return False