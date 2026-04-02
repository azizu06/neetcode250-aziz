class Trie:
    def __init__(self):
        self.children = {}
        self.word = ""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root = Trie()
        for w in wordDict:
            cur = root
            for c in w:
                if c not in cur.children: cur.children[c] = Trie()
                cur = cur.children[c]
            cur.word = w
        res, path = [], []
        def dfs(i):
            if i == len(s):
                res.append(" ".join(path[:]))
                return
            cur = root
            for j in range(i, len(s)):
                if s[j] not in cur.children: break
                cur = cur.children[s[j]]
                if cur.word:
                    path.append(cur.word)
                    dfs(j+1)
                    path.pop()
        dfs(0)
        return res