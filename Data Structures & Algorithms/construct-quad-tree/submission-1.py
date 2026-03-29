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
        def rec(n, r, c):
            if n == 1: return Node(grid[r][c] == 1, True)
            n//=2
            topLeft = rec(n, r, c)
            topRight = rec(n, r, c+n)
            botLeft = rec(n, r+n, c)
            botRight = rec(n, r+n, c+n)
            if topLeft.isLeaf and topRight.isLeaf and botLeft.isLeaf and botRight.isLeaf and topLeft.val == topRight.val == botLeft.val == botRight.val:
                return topLeft
            return Node(False, False, topLeft, topRight, botLeft, botRight)
        return rec(len(grid), 0, 0)

        

        