class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPal(s):
            l, r = 0, len(s)-1
            while l < r:
                if s[l] != s[r]: return False
                l, r = l+1, r-1
            return True
        res = []
        def rec(i, path):
            if i == len(s): 
                res.append(path[:])
                return
            for j in range(i, len(s)):
                if isPal(s[i:j+1]):
                    path.append(s[i:j+1])
                    rec(j+1, path)
                    path.pop()
        rec(0, [])
        return res
