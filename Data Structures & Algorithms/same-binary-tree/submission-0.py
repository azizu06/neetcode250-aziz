# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p1, q1 = [], []
        def dfs(root, arr):
            if not root:
                arr.append(None)
                return
            arr.append(root.val)
            dfs(root.left, arr)
            dfs(root.right, arr)
        dfs(p, p1)
        dfs(q, q1)
        return p1 == q1