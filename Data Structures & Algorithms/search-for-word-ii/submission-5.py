class Trie:
    def __init__(self):
        self.children = {}
        self.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for w in words:
            cur = root
            for c in w:
                if c not in cur.children: cur.children[c] = Trie()
                cur = cur.children[c]
            cur.word = w
        def dfs(cur, r, c):
            if cur.word:
                res.append(cur.word)
                cur.word = ""
            temp = board[r][c]
            board[r][c] = '.'
            steps = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for y, x in steps:
                nr, nc = r+y, c+x
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols: continue
                if board[nr][nc] not in cur.children: continue
                dfs(cur.children[board[nr][nc]], nr, nc)
            board[r][c] = temp

        res = []
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    cur = root.children[board[r][c]]
                    dfs(cur, r, c)
        return res