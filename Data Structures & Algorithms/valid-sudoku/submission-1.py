class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSeen = defaultdict(set)
        colSeen = defaultdict(set)
        gridSeen = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in rowSeen[i]:
                        return False
                    rowSeen[i].add(board[i][j])
                    index = (i//3)*3+(j//3)
                    if board[i][j] in gridSeen[index]:
                        return False
                    gridSeen[index].add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in colSeen[i]:
                        return False
                    colSeen[i].add(board[j][i])    
        return True