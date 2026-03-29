# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res, s1, s2, cur = [], [root], [], root
        while s1:
            s2.append(s1.pop())
            if s2[-1].left:
                s1.append(s2[-1].left)
            if s2[-1].right:
                s1.append(s2[-1].right)
        while s2:
            res.append(s2.pop().val)
        return res
        