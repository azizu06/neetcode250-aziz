class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            if not carry:
                res.append(digits[i])
                continue
            if digits[i] < 9:
                res.append(digits[i]+1)
                carry = 0
            else:
                res.append(0)
        if carry:
            res.append(1)
        return res[::-1]
