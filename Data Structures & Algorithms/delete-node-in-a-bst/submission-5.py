# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root or (root.val == key and not root.left and not root.right): return None
        prev = cur = root
        while cur and cur.val != key:
            prev = cur
            cur = cur.left if cur.val > key else cur.right
        if not cur: return root
        if not cur.left and not cur.right:
            if prev.left == cur:
                prev.left = prev.left.left
            elif prev.right == cur:
                prev.right = prev.right.right
        elif cur.left and not cur.right:
            cur.val = cur.left.val
            prev.left = prev.left.left
        elif cur.right and not cur.right:
            cur.val = cur.right.val
            prev.right = prev.right.right
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
            
        