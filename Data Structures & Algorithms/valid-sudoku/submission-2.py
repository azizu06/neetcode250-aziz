class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        grids = defaultdict(set)
        for r in range(9):
            for c in range(9):
                sq = board[r][c]
                if sq == '.':
                    continue
                grid = (r//3) * 3 + (c//3)
                if sq in grids[grid] or sq in row[r] or sq in col[c]:
                    return False
                row[r].add(sq)
                col[c].add(sq)
                grids[grid].add(sq)
        return True


