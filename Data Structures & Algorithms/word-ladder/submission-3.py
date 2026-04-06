class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        masked = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i]+'.'+w[i+1:]
                masked[pattern].append(w)
        q = deque([(beginWord,1)])
        visit = set([beginWord])
        while q:
            w,steps = q.popleft()
            if w == endWord: return steps
            for i in range(len(w)):
                pattern = w[:i]+'.'+w[i+1:]
                for nei in masked[pattern]:
                    if nei in visit: continue
                    q.append((nei,steps+1))
                    visit.add(nei)
        return 0
            