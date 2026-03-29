class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i in range(len(strs)):
            freq = [0]*26
            for c in strs[i]:
                freq[ord(c)-ord('a')]+=1
            anagrams[tuple(freq)].append(strs[i])
        return list(anagrams.values())
        


