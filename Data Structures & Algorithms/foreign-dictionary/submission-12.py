class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def compare(s1,s2):
            n = min(len(s1),len(s2))
            if s1[:n] == s2[:n] and len(s1) > len(s2): return -1
            for i in range(n):
                if s1[i] != s2[i]: return [s1[i],s2[i]]
            return []
        adj = {c: set() for w in words for c in w}
        indeg = {c: 0 for c in adj}
        for i in range(len(words)-1):
            s1,s2 = words[i],words[i+1]
            chars = compare(s1,s2)
            if chars == -1: return ""
            if not chars: continue
            c1,c2 = chars
            if c2 not in adj[c1]:
                adj[c1].add(c2)
                indeg[c2]+=1
        res = []
        q = deque(c for c in indeg if not indeg[c])
        while q:
            c = q.popleft()
            res.append(c)
            for nei in adj[c]:
                indeg[nei]-=1
                if not indeg[nei]: q.append(nei)
        return "".join(res) if len(res) == len(indeg) else ""
