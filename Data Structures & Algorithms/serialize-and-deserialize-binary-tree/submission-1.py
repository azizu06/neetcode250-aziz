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
        res = ''
        dq = deque([root])
        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()
                if node:
                    res+='#'+str(node.val)
                    dq.append(node.left)
                    dq.append(node.right)
                else:
                    res+='!'
        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: return None
        i = 1
        cur, i = self.getNum(i, data)
        root = TreeNode(int(cur))
        dq = deque([root])
        while dq and i < len(data):
            node = dq.popleft()
            if data[i] == '#':
                cur, i = self.getNum(i+1, data)
                node.left = TreeNode(int(cur))
                dq.append(node.left)
            elif data[i] == '!':
                i+=1
            if i < len(data) and data[i] == '#':
                cur, i = self.getNum(i+1, data)
                node.right = TreeNode(int(cur))
                dq.append(node.right)
            elif data[i] == '!':
                i+=1
        return root
    
    def getNum(self, i, data):
        cur = ''
        while i < len(data) and data[i] != '#' and data[i] != '!':
            cur+=data[i]
            i+=1
        return cur, i

            

