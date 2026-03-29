class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, n, r = 0, 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l+=1
                r-=1
            elif n == 0 and s[l+1:r+1] == s[l+1:r+1][::-1]:
                n = 1
                l+=1
            elif n == 0 and s[l:r] == s[l:r][::-1]:
                n = 1
                r-=1
            else:
                return False
        return True
