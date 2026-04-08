class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        L = R = 0
        for i in range(n):
            l,r = i,i
            while l >= 0 and r < n and s[l] == s[r]:
                if r-l > R-L: L,R = l,r
                l,r = l-1,r+1  
            l,r = i,i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if r-l > R-L:L,R = l,r
                l,r = l-1,r+1
        return s[L:R+1]
        


