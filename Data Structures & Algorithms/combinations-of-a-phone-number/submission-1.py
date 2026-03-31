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
            for c in letters[digits[i]]:
                path.append(c)
                dfs(i+1, path)
                path.pop()
        if digits: dfs(0, [])
        return res