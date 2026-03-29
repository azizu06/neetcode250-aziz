class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq1, freq2 = [0]*26, [0]*26
        for i in range(len(s1)):
            i1, i2 = ord(s1[i])-ord('a'), ord(s2[i])-ord('a')
            freq1[i1], freq2[i2] = freq1[i1]+1, freq2[i2]+1
        matches = 0
        for i in range(26):
            matches += (1 if freq1[i] == freq2[i] else 0)
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            i = ord(s2[r])-ord('a')
            freq2[i]+=1
            if freq1[i] == freq2[i]:
                matches+=1
            elif freq1[i]+1 == freq2[i]:
                matches-=1
            i = ord(s2[l])-ord('a')
            freq2[i]-=1
            if freq1[i] == freq2[i]:
                matches+=1
            elif freq1[i]-1 == freq2[i]:
                matches-=1
            l+=1
        return matches == 26
            
            
                       
