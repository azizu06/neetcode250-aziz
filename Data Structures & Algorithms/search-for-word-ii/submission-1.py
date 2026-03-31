class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for w in words:
            cur = root
            for c in w:
                if c not in cur.children: cur.children[c] = Trie()
                cur = cur.children[c]
            cur.end = True
        def dfs(cur, r, c, word):
            if cur.end: res.add(word)
            seen.add((r,c))
            steps = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for y, x in steps:
                nr, nc = r+y, c+x
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in seen: continue
                if board[nr][nc] not in cur.children: continue
                dfs(cur.children[board[nr][nc]], nr, nc, word+board[nr][nc])
            seen.discard((r,c))
        [["o","a","b","n"],
        ["o","t","a","e"],
        ["a","h","k","r"],
        ["a","f","l","v"]]

        res = set()
        seen = set()
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    cur = root.children[board[r][c]]
                    dfs(cur, r, c, board[r][c])
        return list(res)