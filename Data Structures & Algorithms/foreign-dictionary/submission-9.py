class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def compare(s1,s2):
            n = min(len(s1),len(s2))
            res = []
            for i in range(n):
                if not res and s1[i] != s2[i]: res = [s1[i],s2[i]]
            return res
        adj = defaultdict(list)
        indeg = defaultdict(int)
        for w in words:
            for c in w:
                indeg[c] = 0
        for i in range(len(words)-1):
            s1,s2 = words[i],words[i+1]
            chars = compare(s1,s2)
            print(chars)
            if not chars and len(s1) > len(s2): return ""
            if not chars: continue
            c1,c2 = chars
            adj[c1].append(c2)
            indeg[c2]+=1
        res = []
        print(indeg)
        q = deque(c for c in indeg if not indeg[c])
        while q:
            c = q.popleft()
            res.append(c)
            for nei in adj[c]:
                indeg[nei]-=1
                if not indeg[nei]: q.append(nei)
        return "".join(res) if len(res) == len(indeg) else ""
