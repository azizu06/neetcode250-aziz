# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        prev, cur = None, root
        while cur and cur.val != key:
            prev = cur
            cur = cur.left if cur.val > key else cur.right
        if not cur: return root
        if not cur.left or not cur.right:
            child = cur.left if cur.left else cur.right
            if not prev: return child
            if prev.left == cur:
                prev.left = child
            elif prev.right == cur:
                prev.right = child
        else:
            prev, temp = cur, cur.right
            while temp.left:
                prev = temp
                temp = temp.left
            cur.val = temp.val
            if prev == cur:
                prev.right = prev.right.right
            else:
                prev.left = prev.left.left
        return root
            
        