class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def rec(op, cl, path):
            if op == cl == n:
                res.append("".join(path[:]))
                return
            if op < n:
                path.append('(')
                rec(op+1, cl, path)
                path.pop()
            if cl < op:
                path.append(')')
                rec(op, cl+1, path)
                path.pop()
        rec(0, 0, [])
        return res
