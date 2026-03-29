class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for word in strs:
            letters = [0] * 26
            for letter in range(len(word)):
                letters[ord(word[letter]) - ord('a')] += 1
            key = tuple(letters)
            if key not in freq:
                freq[key] = []
                freq[key].append(word)
            else:
                freq[key].append(word)

        return list(freq.values())

