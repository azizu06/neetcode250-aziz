class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = {}
        def isPal(l,r):
            if (l,r) in memo: return memo[(l,r)]
            if l >= r: return True
            if s[l] != s[r]: return False
            memo[(l,r)] = isPal(l+1,r-1)
            return memo[(l,r)]
        res = s[0]
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if isPal(i,j) and j-i+1 > len(res):
                    res = s[i:j+1]
        return res