# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(root, low, high):
            nonlocal res
            if not root: return
            if not low < root.val < high:
                res = False
                return 
            dfs(root.left, low, root.val)
            dfs(root.right, root.val, high)
        dfs(root, float('-inf'), float('inf'))
        return res
