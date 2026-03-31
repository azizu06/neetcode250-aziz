class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def dfs(i, r, c):
            if board[r][c] != word[i]: return False
            if i == len(word)-1: return True
            temp = board[r][c]
            board[r][c] = '.'
            steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for y, x in steps:
                nr, nc = r+y, c+x
                if 0 <= nr < rows and 0 <= nc < cols:
                    if dfs(i+1, nr, nc): return True
            board[r][c] = temp
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(0, r, c): return True
        return False