class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        resL, resR, minWin = -1, -1, len(s)+1
        sMap, tMap, req = {}, {}, set(t)
        for c in t: tMap[c] = tMap.get(c, 0)+1
        l = matches = 0
        for r in range(len(s)):
            if s[r] in tMap: 
                sMap[s[r]] = sMap.get(s[r], 0)+1
                if tMap[s[r]] == sMap[s[r]]: matches+=1
            if matches == len(req):
                if r-l+1 < minWin: minWin, resL, resR = r-l+1, l, r
                while matches == len(req):
                    if s[l] in sMap:
                        sMap[s[l]]-=1
                        if sMap[s[l]] < tMap[s[l]]: matches-=1
                    l+=1
                    if matches == len(req) and r-l+1 < minWin: minWin, resL, resR = r-l+1, l, r
        if matches == len(t) and len(t)-l < minWin: resL, resR = l, len(t)-1
        return "" if resL+resR<0 else s[resL:resR+1] 

