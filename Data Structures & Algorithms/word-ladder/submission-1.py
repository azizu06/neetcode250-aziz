class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def valid(s1,s2):
            if len(s1) != len(s2): return False
            diff = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]: diff+=1
                if diff > 1: return False
            return True
        words = set(wordList)
        if endWord not in words: return 0
        adj = defaultdict(set)
        for w in wordList:
            if valid(beginWord,w):
                adj[beginWord].add(w)
                adj[w].add(beginWord)
        for i,w in enumerate(wordList):
            for j in range(i+1, len(wordList)):
                if valid(w,wordList[j]):
                    adj[w].add(wordList[j])
                    adj[wordList[j]].add(w)
        print(adj)
        q = deque([(beginWord,1)])
        visit = set([beginWord])
        while q:
            w,steps = q.popleft()
            print(w)
            if w == endWord: return steps
            for nei in adj[w]:
                if nei in visit: continue
                q.append((nei,steps+1))
                visit.add(nei)
        return 0
            