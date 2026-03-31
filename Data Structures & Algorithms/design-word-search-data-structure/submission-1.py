class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children: cur.children[c] = Trie()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(start, root):
            if not root: return False
            for i in range(start, len(word)):
                if word[i] != '.' and word[i] not in root.children: return False
                if word[i] != '.': 
                    root = root.children[word[i]]
                else:
                    for child in root.children.values():
                        if dfs(i+1, child): return True
                    return False
            return root.end
        cur = self.root
        return dfs(0, cur)
    
    

