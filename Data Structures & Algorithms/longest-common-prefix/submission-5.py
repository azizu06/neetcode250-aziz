class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(len(strs)):
                if len(strs[j]) <= i:
                    return prefix
                if char != strs[j][i]:
                    return prefix
            prefix += char
        return prefix


