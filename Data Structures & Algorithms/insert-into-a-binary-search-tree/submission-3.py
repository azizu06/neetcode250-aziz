# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        if not root: return node
        cur = root
        while cur.left or cur.right:
            if cur.left and val < cur.val:
                cur = cur.left
            elif cur.right and val > cur.val:
                cur = cur.right
            else:
                break
        if val < cur.val:
            cur.left = node
        elif val > cur.val:
            cur.right = node
        return root

        
