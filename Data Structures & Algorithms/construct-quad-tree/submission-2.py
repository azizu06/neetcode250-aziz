"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def checkGrid(n, r, c):
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]: return False
            return True

        def rec(n, r, c):
            if checkGrid(n, r, c): return Node(grid[r][c], True)
            n//=2
            topLeft = rec(n, r, c)
            topRight = rec(n, r, c+n)
            botLeft = rec(n, r+n, c)
            botRight = rec(n, r+n, c+n)
            return Node(1, False, topLeft, topRight, botLeft, botRight)
        return rec(len(grid), 0, 0)


        

        