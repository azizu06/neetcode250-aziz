class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def build(s):
            res = []
            for i in range(len(s)):
                t = list(s)
                t[i] = '.'
                res.append("".join(t))
            return res
        masked = defaultdict(list)
        for w in wordList:
            comb = build(w)
            for c in comb:
                masked[c].append(w)
        q = deque([(beginWord,1)])
        visit = set([beginWord])
        while q:
            w,steps = q.popleft()
            if w == endWord: return steps
            comb = build(w)
            for c in comb:
                for nei in masked[c]:
                    if nei in visit: continue
                    q.append((nei,steps+1))
                    visit.add(nei)
        return 0
            