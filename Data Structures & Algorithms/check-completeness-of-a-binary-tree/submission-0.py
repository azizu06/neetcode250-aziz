# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        end = False
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    end = True
                else: 
                    if end: return False
                    q.append(node.left)
                    q.append(node.right)
        return True