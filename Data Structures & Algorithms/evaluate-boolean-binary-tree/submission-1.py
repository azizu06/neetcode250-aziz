# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return False
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            if not root.left and not root.right:
                return True if root.val == 1 else False
            else:
                return root.left or root.right if root.val == 2 else root.left and root.right
            return root
        return dfs(root)