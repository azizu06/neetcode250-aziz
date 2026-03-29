class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        len1, len2 = len(word1), len(word2)
        l = r = 0
        turn = True
        while l < len1 and r < len2:
            if turn == True:
                res += word1[l]
                l+=1
            else:
                res += word2[r]
                r+=1
            turn = not turn
        while l < len1:
            res += word1[l]
            l+=1
        while r < len2:
            res += word2[r]
            r+=1
        return res