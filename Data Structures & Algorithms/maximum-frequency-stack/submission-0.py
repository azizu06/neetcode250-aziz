class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.s = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freq[val]+=1
        if self.freq[val] > self.maxFreq:
            self.maxFreq = self.freq[val]
            self.s[self.maxFreq].append(val)
        else:
            self.s[self.freq[val]].append(val)
        

    def pop(self) -> int:
        res = self.s[self.maxFreq].pop()
        self.freq[res]-=1
        if not self.s[self.maxFreq]:
            self.maxFreq-=1
        return res

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()