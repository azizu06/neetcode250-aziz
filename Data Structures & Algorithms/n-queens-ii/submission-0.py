class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        pos, neg, col = set(), set(), set()
        def dfs(r):
            nonlocal res
            if r == n:
                res+=1
                return
            for c in range(n):
                if c in col or (r+c) in pos or (r-c) in neg: continue 
                col.add(c)
                pos.add(r+c)
                neg.add(r-c)
                dfs(r+1)
                col.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)
        dfs(0)
        return res

            