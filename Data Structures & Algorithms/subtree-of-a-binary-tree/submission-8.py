# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(r1, r2):
            if not r1 and not r2: return True
            if r1 and r2 and r1.val == r2.val:
                return isSame(r1.left, r2.left) and isSame(r1.right, r2.right)
            return False
        res = False
        def dfs(root):
            nonlocal res
            if not root: return
            if root.val == subRoot.val and isSame(root, subRoot):
                res = True
                return
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res

