class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            length = str(len(strs[i]))
            strs[i] = length + '!' + strs[i]
        strs = "".join(strs)
        return strs

    def decode(self, s: str) -> List[str]:
        arr = []
        i = 0
        num = ''
        while i < len(s):
            if(s[i] != '!'):
                num += s[i]
                i+=1
            else:
                num = int(num)
                arr.append(s[i+1:i+num+1])
                i += num+1
                num = ''
        return arr
            