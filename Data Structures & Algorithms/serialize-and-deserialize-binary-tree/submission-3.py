# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ''
        res = []
        dq = deque([root])
        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()
                if node:
                    res.append(str(node.val))
                    dq.append(node.left)
                    dq.append(node.right)
                else:
                    res.append('!')
        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: return None
        data = data.split(',')
        root = TreeNode(int(data[0]))
        dq = deque([root])
        i = 1
        while dq:
            node = dq.popleft()
            if data[i] != '!':
                node.left = TreeNode(int(data[i]))
                dq.append(node.left)
            i+=1
            if data[i] != '!':
                node.right = TreeNode(int(data[i]))
                dq.append(node.right)
            i+=1
        return root

            

