class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        def dfs(i, path):
            if len(path) == len(digits):
                res.append("".join(path[:]))
                return
            for j in range(i, len(digits)):
                for c in letters[digits[j]]:
                    path.append(c)
                    dfs(j+1, path)
                    path.pop()
        if not digits: return []
        dfs(0, [])
        return res