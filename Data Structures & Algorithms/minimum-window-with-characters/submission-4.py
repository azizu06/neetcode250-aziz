class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        resL, resR, minWin = -1, -1, len(s)+1
        sMap, tMap = {}, {}
        for c in t: tMap[c] = tMap.get(c, 0)+1
        l = matches = 0
        for r in range(len(s)):
            if s[r] in tMap: 
                sMap[s[r]] = sMap.get(s[r], 0)+1
                if tMap[s[r]] == sMap[s[r]]: matches+=1
            while matches == len(tMap):
                if matches == len(tMap) and r-l+1 < minWin: minWin, resL, resR = r-l+1, l, r
                if s[l] in sMap:
                    sMap[s[l]]-=1
                    if sMap[s[l]] < tMap[s[l]]: matches-=1
                l+=1
        return "" if resL+resR<0 else s[resL:resR+1] 

