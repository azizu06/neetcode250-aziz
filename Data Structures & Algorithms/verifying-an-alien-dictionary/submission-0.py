class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letters = {c: i for i, c in enumerate(order)}
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]): return False
                a, b = words[i][j], words[i+1][j]
                if letters[b] < letters[a]:
                    return False
                elif letters[b] > letters[a]:
                    break
        return True
