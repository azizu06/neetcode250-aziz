# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, best):
            nonlocal res
            if not root: return
            if root.val >= best: res+=1
            dfs(root.left, max(best, root.val))
            dfs(root.right, max(best, root.val))
        dfs(root, root.val)
        return res