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
        def checkGrid(r1, c1, r2, c2, grid):
            for i in range(r1, r2):
                for j in range(c1, c2):
                    if grid[i][j] != grid[r1][c1]: return False
            return True

        def rec(r1, c1, r2, c2, grid):
            if checkGrid(r1, c1, r2, c2, grid): return Node(grid[r1][c1], True, None, None, None, None)
            midR, midC = (r1+r2)//2, (c1+c2)//2
            topLeft = rec(r1, c1, midR, midC, grid)
            topRight = rec(r1, midC, midR, c2, grid)
            botLeft = rec(midR, c1, r2, midC, grid)
            botRight = rec(midR, midC, r2, c2, grid)
            return Node(1, False, topLeft, topRight, botLeft, botRight)
        return rec(0, 0, len(grid), len(grid), grid)

        

        