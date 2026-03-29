# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def dfs(root):
            nonlocal res
            if not root: return 0
            left, right = dfs(root.left), dfs(root.right)
            paths = [root.val, root.val+left, root.val+right, root.val+left+right]
            res = max(res, max(paths))
            return root.val+max(left,right,0)
        dfs(root)
        return res