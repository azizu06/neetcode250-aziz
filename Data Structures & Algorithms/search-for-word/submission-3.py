class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def dfs(i, r, c):
            if i == len(word): return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False
            temp = board[r][c]
            board[r][c] = '.'
            steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for y, x in steps:
                nr, nc = r+y, c+x
                if dfs(i+1, nr, nc): return True
            board[r][c] = temp
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(0, r, c): return True
        return False