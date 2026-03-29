class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res, total = [], 0
        for o in operations:
            if o == '+':
                res.append(res[-1] + res[-2])
            elif o == 'D':
                res.append(2*res[-1])
            elif o == 'C':
                res.pop()
            else:
                res.append(int(o))
        for n in res:
            total += n
        return total

