class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i,j = len(a)-1,len(b)-1
        carry = 0
        res = []
        while max(i,j) >= 0 or carry:
            n1 = 0 if i < 0 else int(a[i])
            n2 = 0 if j < 0 else int(b[j])
            total = n1+n2+carry
            bit,carry = total%2,total//2
            res.append(str(bit))
            i,j = i-1,j-1
        return ''.join(res[::-1])

