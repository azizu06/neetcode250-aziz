class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        f1, f2 = [0]*26, [0]*26
        for i in range(len(s1)):
            f1[ord(s1[i])-ord('a')]+=1
            f2[ord(s2[i])-ord('a')]+=1
        match = l = 0
        for i in range(26):
            if f1[i] == f2[i]:
                match+=1
        for i in range(len(s1), len(s2)):
            if match == 26:
                return True
            idx = ord(s2[i])-ord('a')
            f2[idx]+=1
            if f1[idx] == f2[idx]:
                match+=1
            elif f1[idx]+1 == f2[idx]:
                match-=1
            idx = ord(s2[l])-ord('a')
            f2[idx]-=1
            if f1[idx] == f2[idx]:
                match+=1
            elif f1[idx]-1 == f2[idx]:
                match-=1
            l+=1
        return match == 26
            
            
            
